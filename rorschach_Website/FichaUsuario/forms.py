# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:49:05 2017

@author: Dylan N. Sugimoto
"""

from .models import UserInfo
from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    
    name = forms.CharField(label = "name", max_length = 250)
    username = forms.CharField(label = "username", max_length = 250)
    age = forms.IntegerField(min_value = 0, max_value = 130)
    email_account = forms.EmailField(label = "email_account",max_length = 150, 
                                     required = False,
                                     validators = [EmailValidator])
    country = forms.CharField(label = "country", max_length = 150)
    home_state_adress = forms.CharField(label = "home_state_adress", max_length = 150)
    religion = forms.CharField(label = "religion", max_length = 150)
    civil_status = forms.CharField(label = "civil_status", max_length = 150)
    profession = forms.CharField(label = "profession", max_length = 150)
    gender = forms.CharField(label="gender", max_length = 10)
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        #informacao sobre a classe
        model = UserInfo
        fields = ['name','username', 'email_account', 'password', 'country', 
                  'home_state_adress', 'religion','civil_status', 'profession',
                  'gender', 'age']
    def clean(self):
        #metodo para verificar validade de dados do usuario
        cleaned_data = super(UserForm,self).clean()
        email = cleaned_data.get("email_account")
        user = UserInfo.objects.filter(email_account = email)
        if user:
            print("error2")
            print(user)
            raise forms.ValidationError("This email account already exist.")
        
        return cleaned_data


class loginForm(forms.ModelForm):
    
    password = forms.CharField(widget = forms.PasswordInput)
    login = forms.CharField(label = "login", max_length = 150)
    
    class Meta:
        
        model = User
        fields = ['login', 'password']