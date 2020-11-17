# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
# from aplications.inputapp.models import *
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .forms import RegisterForm, UpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import *

 
def portada(request):
        return render(request,'mainapp/portada.html',{
        'title':'Start'
    })
# @login_required
def index(request):
    return render(request,'mainapp/index.html',{
        'title':'Presentation'
    })
    
def register_form(request):
    
    register_form = RegisterForm()
    
    #Se usa para ver si el formulario funciona bien
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            messages.success(request,"Correct registration")
            
            return redirect('inicio')
    
    return render(request, 'mainapp/user/register.html',{
        'title' : 'Register',
        'register_form': register_form
    })

def login_form(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)

        if user is not None: 
            login(request,user)
            return redirect('mainapp:inicio')
        
        else:
            messages.warning(request,'You have not logged in correctly')
    
    return render(request, 'mainapp/user/login.html',{
        'title' : 'Login'
    })
# @login_required
def logout_user(request):
    logout(request)
    return redirect('mainapp:portada')


def update_form(request):
    
    update_form = UpdateForm()
    
    #Se usa para ver si el formulario funciona bien
    if request.method == 'POST':
        update_form = UpdateForm(request.POST)
        
        if update_form.is_valid():
            update_form.save()
            messages.success(request,"Correct  update profile")
            
            return redirect('mainapp:inicio')
    return render(request, 'mainapp/user/editProfile.html',{
        'title' : 'Edit Profile',
        'update_form': update_form
    })