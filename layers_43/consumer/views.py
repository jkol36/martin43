from django.shortcuts import render_to_response
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render_to_response('index.html', {})


# show discussion
def show_discussion(request):
    return HttpResponse('')


# send a simple text based message
def send_message(request):
    return HttpResponse('')


# show discussion items before an id
def discussion_before(request, id):
    return HttpResponse('')


# pay the deposit
def process_deposit(request):
    return HttpResponse('')


# add photo to idea board
def add_photo_to_idea_board(request):
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
