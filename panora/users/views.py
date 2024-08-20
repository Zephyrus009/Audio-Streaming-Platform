from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == "POST":
        user = request.POST.get('full-name')
        password = request.POST.get('password')
        auth_user = authenticate(request,username = user,password = password)
        if auth_user is not None:
            login(request,auth_user)
            return redirect(reverse('audio_streamer:panora_home'))
        else:
            messages.error(request,'User Not Found, Please Register User !')
            return render(request,'users/login_page.html')
    else:
        return render(request,'users/login_page.html')

def register_view(request):
    if request.method == 'POST':
        user = request.POST.get('full-name')
        password = request.POST.get('password')
        if len(user) > 0 and len(password) > 0:
            create_user = User.objects.create_user(username=user,password=password)
            create_user.save()
        else:
            messages.error(request,'Please add proper username and password')
            return render(request,'users/register_page.html')
    else:
        return render(request,'users/register_page.html')

def logout_view(request):
    logout(request)
    return render(request,'home.html')
