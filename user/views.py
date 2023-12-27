from django.shortcuts import render, redirect
from .import forms
from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method=='POST':
        form= forms.Register(request.POST)
        if form.is_valid():
            messages.success(request,'Account created successfully')
            form.save()
            return redirect('login')
        
    form= forms.Register()
    return render(request, 'register.html', {'form': form, 'type': 'Sign Up'})

def user_login(request):
    if request.method=='POST':
        form= AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name= form.cleaned_data['username']
            user_pass= form.cleaned_data['password']
            
            user= authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged In Successfully')
                login(request,user)
                return redirect('profile')
            
            else:
                messages.warning(request, 'Wrong info. Try again')
                return redirect('register')
        
    form= AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type': 'Log In'})

def user_logout(request):
    messages.success(request, 'Logged out Successfully')
    logout(request)
    return redirect('login')

def change_pass_with_old(request):
    if request.method=='POST':
        form= PasswordChangeForm(user=request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        
    form= PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html', {'form': form})

def change_pass_without_old(request):
    if request.method=='POST':
        form= SetPasswordForm(user=request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        
    form= SetPasswordForm(user=request.user)
    return render(request, 'change_pass.html', {'form': form})
            
               
 
                