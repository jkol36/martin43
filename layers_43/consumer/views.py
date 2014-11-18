from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django_ajax.decorators import ajax
from django.contrib.auth.models import User
from models import Project
from forms import new_designForm, picture_form, UserForm, PassWordForm



# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return redirect('submit_design')
    else:
        return redirect('login')


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

def signup(request):
    if request.user.is_authenticated():
        return redirect('idea_bored')
    if request.POST:
        try:
            print request.POST
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            if password1 != password2:
                return HttpResponse('Your passwords did not match')
            if "@" not in email:
                return HttpResponse('You did not type in a valid email address')
            form = PassWordForm(request.POST)
            if form.is_valid():
                password1 = form.cleaned_data['password']
                print password1
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    return HttpResponse("Your password's did not match.")
                else:
                    new_user_instance = User.objects.create_user(username=email, password=password1, first_name=first_name, last_name=last_name)
                return redirect('login')
            
            
        except Exception, e:
            return HttpResponse('Your email already exists perhaps try logging in.')
    return render(request, 'signup.jade', 'forms':forms)

#logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# submit a new design
def submit_design(request):
    user = request.user
    authenticated = user.is_authenticated()
    print authenticated
    forms = {'submit_design':new_designForm, 'password_form':PassWordForm, 'user_form':UserForm, 'picture_form':picture_form}
    if request.POST:
        print request.FILES
        if authenticated == True:
            try:
                email = request.user.username
                description = request.POST['description']
                if description:
                    print description
                else:
                    return HttpResponse('You did not give your product a description!')
                ship_date = request.POST['deadline']
                if ship_date:
                    month = ship_date[0:2]
                    day = ship_date[3:5]
                    year = ship_date[6:10]
                    format_date = "%s-%s-%s" %(year, month, day)    
                budget = request.POST['budget']
                if budget:
                    print budget
                else:
                    pass
                pictureform = picture_form(request.POST, request.FILES)
                if pictureform.is_valid():
                    pass
                else:
                    print pictureform.errors
                lookup_user = User.objects.get(username=email)
                new_project = Project.objects.create(user=lookup_user, photo=request.FILES['photo'], description=description, budget=budget, deadline=format_date)
                new_project.save()
                return HttpResponse('Thank you. Your info has been recieved!')
            except Exception, e:
                print e

            return render(request, 'forms.jade', {'forms':forms, 'authenticated':authenticated})
        elif authenticated == False:
            print 'authenticated false' 
            try:
                email = request.POST['email']
                print email
                description = request.POST['description']
                if description:
                    print description
                else:
                    return HttpResponse('You did not give your product a description!')
                ship_date = request.POST['deadline']
                if ship_date:
                    month = ship_date[0:2]
                    day = ship_date[3:5]
                    year = ship_date[6:10]
                    format_date = "%s-%s-%s" %(year, month, day)
                else:
                    return HttpResponse('No ship date')
                budget = request.POST['budget']
                print 'budget'
                photo = picture_form(request.POST, request.FILES)
                if photo.is_valid():
                    pass
                else:
                    print photo.errors
                #check to see if the user already has an account, create an account for them if they don't
                try:
                    user, created = User.objects.get_or_create(username=email, email=email)
                    if created == True:
                        add_project = Project.objects.create(user=user, photo=request.FILES['photo'], description=description, budget=budget, deadline=format_date)
                        created = True
                        return render(request, 'signup.jade', {'design_object':created, 'forms':forms, 'email':user})
                    else:
                        add_project = Project.objects.create(user=user, photo=request.FILES['photo'], description=description, budget=budget, deadline=format_date)
                        created = True
                        return render(request, 'signup.jade', {'design_object':created, 'forms':forms, 'email':user})
                #return any errors that may arise during the lookup/create account process
                except Exception, e:
                  print e
            #return any errors that may occur during the submit form process
            except Exception, e:
                print e

    return render(request, 'forms.jade', {'forms':forms})
                    
#find designer view
def find_designer(request):
    if request.POST:
        email = request.POST['design_object']
        if email:
            user_instance = User.objects.get(email=email)
        else:
            return HttpResponse("email cannot be left blank")
        first_name = request.POST['first_name']
        if first_name:
            user_instance.first_name = first_name
        else:
            return HttpResponse("You left first name blank")
        last_name = request.POST['last_name']
        if last_name:
            user_instance.last_name = last_name
        else:
            return HttpResponse('you left last name blank!')
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user_instance.password = password1
        else:
            return HttpResponse("Your passwords did not match.")
        user_instance.save()
        print user_instance
        return HttpResponse("Awesome thanks.")


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
        return render(request, 'idea_bored.jade', {'projects':projects})
    else:
        pass
    return render(request, 'idea_bored.jade')


# show discussion
def show_discussion(request):
    return HttpResponse('')


# send a simple text based message
def send_message(request):
    return HttpResponse('')


# add a photo
def add_photo(request):
    # http://django-storages.readthedocs.org/en/latest/
    return HttpResponse('')


# show discussion items before an id
def discussion_before(request, msg_id):
    return HttpResponse('')


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
