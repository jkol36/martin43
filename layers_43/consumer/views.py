from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django_ajax.decorators import ajax
from django.contrib.auth.models import User
from models import Project, ProjectUpdateItem, ProjectUpdate
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
    forms = {'password_form':PassWordForm}
    if request.POST:
        try:
            print request.POST
            email = request.POST['email']
            account = User.objects.filter(username=email)
            #Check to see if user has an account.
            if len(account)> 0:
                #if an account shows up
                try:
                    #check to see if the user has a password
                    account_info = account.values()
                    if account_info[0]['password'] == "":
                        pass
                    else:
                        return render(request, 'login.jade', {'account':email})
                except Exception, e:
                    print e
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            if "@" not in email:
                return HttpResponse('You did not type in a valid email address')
            form = PassWordForm(request.POST)
            if form.is_valid():
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    return HttpResponse("Your password's did not match.")
                else:
                    new_user_instance = User.objects.create_user(username=email, password=password1, first_name=first_name, last_name=last_name)
                return redirect('login')
            
        except Exception, e:
            print e
    return render(request, 'signup.jade', {'forms':forms})

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
                lookup_user = User.objects.get(username=email)
                new_project = Project.objects.create(user=lookup_user, description=description, budget=budget, deadline=format_date)
                print new_project.id
                new_project.save()
                #
                #if there's a photo submitted we'll create a new projectupdate_object around the newly created project object
                if request.FILES:
                    pictureform = picture_form(request.POST, request.FILES)
                    if pictureform.is_valid():
                      #get the created project
                        get_project = Project.objects.get(description=description, budget=budget, deadline=format_date)
                        new_projectupdate_object =  ProjectUpdate.objects.create(project=get_project, name=description, user=lookup_user, update_type="picture")
                        new_projectupdate_object.save()
                        #get the created project update object
                        get_project_update = ProjectUpdate.objects.get(project=get_project, name=description, user=lookup_user, update_type="picture")
                        #create a new UpdateItem object
                        new_projectupdateitem_object= ProjectUpdateItem.objects.create(photo=request.FILES['photo'], update=get_project_update)
                        new_projectupdateitem_object.save()
                        print new_projectupdate_object
                    else:
                        print pictureform.errors
                return HttpResponse('Thank you. Your info has been recieved!')
            except Exception, e:
                print e

            return render(request, 'forms.jade', {'forms':forms, 'authenticated':authenticated})
        elif authenticated == False:
            is_user = False
            is_created = False
            try:
                email = request.POST['email']
                account = User.objects.filter(username=email)
                #Check to see if user has an account.
                if len(account)> 0:
                    #if an account shows up
                    try:
                        #check to see if the user has a password
                        account_info = account.values()
                        if account_info[0]['password'] == "":
                            #if they don't have a password, they aren't a real user.
                          is_user = False
                        else:
                            #if they do have password, they are a user
                            is_user = True


                    except Exception, e:
                        print e
                else:
                    pass

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
                #check to see if the user already has an account, create an account for them if they don't
                try:
                    user, created = User.objects.get_or_create(username=email, email=email)
                    if created == True:
                        add_project = Project.objects.create(user=user, description=description, budget=budget, deadline=format_date)
                        is_created = True
                    else:
                        add_project = Project.objects.create(user=user, description=description, budget=budget, deadline=format_date)
                        is_created = False
                #return any errors that may arise during the lookup/create account process
                except Exception, e:
                  print e
                #now that the users project is created lets see if there was any images in the request.POST
                if request.FILES:
                    photo = picture_form(request.POST, request.FILES)
                    if photo.is_valid():
                        #get the created object
                        project = Project.objects.get(user=user, description=description, budget=budget, deadline=format_date)
                        #create a new ProjectUpdateObject
                        new_update = ProjectUpdate.objects.create(project=project, name=description, user=user, update_type="picture")
                        #save the new update object
                        new_update.save()
                        get_update_object = ProjectUpdate.objects.get(project=project, name=description, user=user, update_type="picture")
                        #create a new projectupdateitem object containing the picture uploaded
                        new_picture = ProjectUpdateItem.objects.create(photo=request.FILES['photo'], update=get_update_object)
                        new_picture.save()
                    else:
                        print photo.errors
                else:
                    pass
                #if a new account was created upon signup or they have an account but haven't instantiated it. User must complete registration before being allowed to login.
                if is_created == True:
                    return render(request, 'signup.jade', {'email':user, 'forms':forms})
                elif is_created == False:
                    print is_user
                    try:
                        if is_user == True:
                            i = 1
                            return render(request, 'login.jade', {'design_object': i})
                        elif is_user == False:
                            return render(request, 'signup.jade', {'email':user, 'forms':forms})
                            
                    except Exception, e:
                        print e



            #return any errors that may occur during the submit form process
            except Exception, e:
                print e

    return render(request, 'forms.jade', {'forms':forms})
                    
#find designer view
def find_designer(request):
    if request.POST:
        print request.POST
        try:
            email = request.POST['email']
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
                user_instance.set_password(password1)
            else:
                return HttpResponse("Your passwords did not match.")
            user_instance.save()
            print user_instance
        except Exception, e:
            print e
        return redirect('login')


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
