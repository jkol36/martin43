from django import forms
from django.contrib.auth.models import User
from models import Project, ProjectUpdateItem
from sorl.thumbnail import ImageField


class new_designForm(forms.ModelForm):
	description = forms.CharField(label="description", widget=forms.TextInput(attrs={'id':'description', 'class':'form-control', 'placeholder':'A few words to describe this project like: Confetti for Jenny'}))
	budget = forms.DecimalField(label="budget", widget=forms.NumberInput(attrs={'id':'budget', 'class':'form-control', 'placeholder':'What is your budget?'}))
	deadline = forms.DateField(label="ship date", widget=forms.DateInput(attrs={'id':'ship_date', 'class':'form-control', 'placeholder':'When do you need the designs by?'}))
	class Meta:
		model = Project
		fields = ['description', 'deadline', 'budget']
class picture_form(forms.ModelForm):
	class Meta:
		model= ProjectUpdateItem
		exclude = ['update']

class UserForm(forms.ModelForm):
	email = forms.CharField(label="Your Email", widget=forms.EmailInput(attrs={'id':'email', 'class':'form-control', 'placeholder':'JonDoe@gmail.com'}))

	class Meta:
		model = User
		fields = ['email']
class PassWordForm(forms.ModelForm):
	password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'id':'password1', 'class':'form-control', 'name':'password1', 'placeholder':'enter a password'}))
	password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'id':'password2', 'class':'form-control', 'name':'password2', 'placeholder':'enter it again'}))
	class Meta:
		model = User
		fields = ['password1', 'password2']
