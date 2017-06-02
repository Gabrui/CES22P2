# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:49:05 2017

@author: Dylan N. Sugimoto
"""

from django.contrib.auth.models import User
from django import forms
from django.core.validators import EmailValidator

class UserForm(forms.ModelForm):
    
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
        #information about your class
        model = User
        fields = ['username', 'email_account', 'password', 'country', 
                  'home_state_adress', 'religion','civil_status', 'profession',
                  'gender', 'age']
