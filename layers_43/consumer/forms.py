from django import forms
from django.contrib.auth.models import User
from models import Project
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
		model= Project
		exclude = ['user', 'title', 'zipcode', 'product_type', 'order_quantity', 'materials', 'deadline', 'description', 'budget', 'is_submitted']

class UserForm(forms.ModelForm):
	email = forms.CharField(label="Your Email", widget=forms.EmailInput(attrs={'id':'email', 'class':'form-control', 'placeholder':'JonDoe@gmail.com'}))

	class Meta:
		model = User
		fields = ['email']

