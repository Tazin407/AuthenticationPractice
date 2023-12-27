from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms 

class Register(UserCreationForm):
    class Meta:
        model= User
        fields=['username', 'first_name', 'last_name', 'email']
        

class Update(UserChangeForm):
    class Meta:
        model= User
        fields='__all__'
    