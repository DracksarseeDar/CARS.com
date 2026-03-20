from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User 
from . import forms , models

def register_view(request):
    if request.method == 'POST':
        form = forms.CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = forms.CustomRegisterForm()
    
    return render(
        request,
        'register.html',
        {
            'form': form,
        }
    )

def auth_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/congratulation/')
    else:
        form = AuthenticationForm()
    
    return render(
        request,
        'login.html',
        {
            "form": form,
        }
    )

def auth_logout_view(request):
    logout(request)
    return redirect('/login/')

def cong_view(request):
    
    users_list = models.CustomUser.objects.all() 
    return render(
        request,
        'cong.html',
        {
            'user': users_list
        }
    )