from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login_page")
def home(request):
    return render(request, 'register/home.html')

def regi(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        username = request.POST.get('username')
       
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username is already taken!")
            return redirect('/regi')
        
        user = User.objects.create(
            first_name = first_name,
            username = username,
           
        )
        user.set_password(password)
        user.save()

        return redirect('/login_page')

    return render(request, 'register/regi.html')
    

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.info(request, "invalide username")
            return redirect('/regi')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'invalid password')
            return redirect('/login_page')
        else:
            login(request, user)
            return redirect('/')
    return render(request, 'register/login.html')

def logout_page(request):
    logout(request)
    return render(request, 'register/logout.html')
    #return redirect('/login/')
