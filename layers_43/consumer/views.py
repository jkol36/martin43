from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from models import Project
from forms import new_designForm, picture_form, UserForm



# Create your views here.
def index(request):
    return render_to_response('index.html', {})

# submit a new design

def submit_design(request):
    forms = {'submit_design':new_designForm, 'user_form':UserForm, 'picture_form':picture_form}
    
    if request.POST:
        print request.POST
        email = request.POST['email']
        if email:
            user = User.objects.create(email=email, username=email)
            user.save()
        else:
            return HttpResponse('You did not enter an email address')
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
        photos = picture_form(request.POST, request.FILES)
        budget = request.POST['budget']
        if budget:
            print budget
        else:
            pass
        lookup_user = User.objects.get(username=email)
        new_project = Project.objects.create(user=lookup_user, description=description, budget=budget, deadline=format_date)
        new_project.save()
        

    return render(request, 'forms.jade', {'forms':forms})
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
