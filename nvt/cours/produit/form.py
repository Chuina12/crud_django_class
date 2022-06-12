from dataclasses import fields
from . models import Produit
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Ajout(forms.ModelForm):
    class Meta:
        model = Produit
        fields ='__all__'
        
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
    
        ]
   
  
    