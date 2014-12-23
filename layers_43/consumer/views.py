from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic.base import RedirectView
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from models import Project, ProjectUpdateItem, ProjectUpdate
from forms import new_designForm, picture_form, UserForm, PassWordForm, recipientForm, projectForm
from layers_43.messaging.models import Message



# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return redirect('submit_design')
    else:
        return render(request, 'index.jade')


#login view

def login(request):
    if request.user.is_authenticated():
        return redirect('submit_design')
    if request.POST:
        print request.POST
        email = request.POST['email']
        password = request.POST['password']
        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                auth_login(request, user)
                return redirect('submit_design')
            else:
                return HttpResponse('user with that email/password does not exist')
        return HttpResponse('You did not submit either an email or password')
    return render(request, 'login.jade')

#signup view

def create_user(self, username, password_1, password_2):
    if password_1 ==  password_2:
        password = password_1
        create_or_get_user, _ = User.objects.get_or_create(username=username, email=username)
        create_or_get_user.set_password(password)
        create_or_get_user.save()
        return create_or_get_user
    else:
        return HttpResponse(request, "passwords dont match")
def signup(request):
    if request.user.is_authenticated():
        return redirect('idea_bored')
    if request.POST:
        print request.POST
        username = request.POST['email']
        password_1 = request.POST['password1']
        password_2 = request.POST['password2']
        new_user = create_user(request, username=username, password_1=password_1, password_2=password_2)
        return redirect('login')
    else:
        return render(request, 'signup.jade')


#logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# submit a new design
# user redirected from landing page via get_started button. Or redirect by submit_new_design in my account.
def submit_design(request):
    user = request.user
    authenticated = user.is_authenticated()
    if request.POST:
        #Split the submitted content on white space. Part before the white space is the first name
        #portion after the white space is the last name
        first_name = request.POST.get('name').split()[0]
        last_name = request.POST.get('name').split()[1]
        description = request.POST.get('description')
        title = request.POST.get('title')
        budget = request.POST.get('budget_to')
        due_date= request.POST.get('due_date')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "password don't match")
        else:
            password = password1
        new_user_object, created = User.objects.get_or_create(username=email, email=email, first_name=first_name, last_name=last_name)
        #save the user_id for User object lookup later on
        user_id = new_user_object.id
        #set the password to the submitted password if both password1 and password2 match
        new_user_object.set_password(password)
        #save the object
        new_user_object.save()
        #Get the newly created user object
        get_new_user_object = User.objects.get(pk=user_id)
        #create a new project with a relationship to the user object
        new_project_object, created = Project.objects.get_or_create(title=title, description=description, budget=budget, deadline=due_date, user=get_new_user_object)
        #store the project_id for later lookup
        project_id = new_project_object.id
        #save the project
        new_project_object.save()
        #return inspiration.jade with the project_id and user_id
        return render(request, 'inspiration.jade', {'pk':project_id, 'user':user_id})


    return render(request, 'idea.jade')
                    
#find designer view
def find_designer(request):
   designers = User.objects.filter(is_designer = True, available=True)
   if designers:
        return render(request, 'main.jade', {'designers':designers})
   else:
        messages.errors(request, "Sorry, no designers are available. We'll notify you as soon as one becomes available.")
        


#idea bored
@login_required
def idea_bored(request):
    projects = request.user.projects.all()
    for i in projects:
        print i.photo
    current_project_status = False
    start_new_project = False
    view_design_bored = False
    if projects:
        return render(request, 'inspiration.jade', {'projects':projects})
    else:
        pass
    return render(request, 'inspiration.jade')


# show discussion
def show_discussion(request):
    return HttpResponse('')


# send a simple text based message
def send_message(request):
    return render(request, 'send_message.jade', {'recipient':recipientForm(user=request.user), 'project_form':projectForm(user=request.user.id)})


# add a phot
def inspiration_view(request):

    # http://django-storages.readthedocs.org/en/latest/
    return render(request, 'inspiration.jade')

def add_photo(request):
    if request.FILES:
        #project id for lookup
        project_id = request.POST['pk']
        #user id for lookup
        user_id = request.POST.get('user')
        project = Project.objects.get(pk=project_id)
        for f in request.FILES.getlist('file'):
            user = User.objects.get(pk=user_id)
            #a new update's taking place. In this case it's a picture.
            #create a new update
            new_update = ProjectUpdate.objects.create(project=project, name="picture", user=user, update_type="picture")
            #save the update object id for lookup
            new_update_id = new_update.id
            #save the projectupdate
            new_update.save()
            #get the update using the id
            get_update = ProjectUpdate.objects.get(pk=new_update_id)
            #add a new picture object
            new_picture = ProjectUpdateItem.objects.create(photo=f, update = get_update)
            #save the picture object
            new_picture.save()
        messages.success(request, "Success!")
    return HttpResponse('success')


    





def discussion_before(request, msg_id):
    return HttpResponse('')

#my account view

def my_account(request):
    user_instance = request.user
    projects = Project.objects.filter(user=request.user)
    messages_to = Message.objects.filter(sender = request.user)
    messages_recieved = Message.objects.filter(recipient = request.user)
    if messages_recieved:
        return True
    else:
        return False
    if messages_recieved:
        return True
    else:
        return False
    return render(request, 'my_account.jade', {'messages_to':messages_to, 'messages_recieved':messages_recieved})
# pay the deposit
def process_payment(request):
    return HttpResponse('')


# add photo to inspiration board
def add_photo_to_inspiration_board(request):
    return HttpResponse('')


# accept a proposal
def accept_proposal(request):
    return HttpResponse('')


# reject a proposal
def reject_proposal(request):
    return HttpResponse('')


# accept designer
def accept_designer(request):
    """
    To Be Implemented Later
    """
    return HttpResponse('')


# reject designer
def reject_designer(request):
    """
    To Be Implemented Later
    """
    return HttpResponse('')
