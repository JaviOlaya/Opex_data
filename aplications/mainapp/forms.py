from django import forms 
from django.core import validators

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']

class UpdateForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password']
        