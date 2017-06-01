# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:49:05 2017

@author: Dylan N. Sugimoto
"""

from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        #information about your class
        model = User
        fields = ['username', 'email', 'password']
