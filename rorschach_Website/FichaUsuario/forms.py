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
    """
    Classe que representa o formulario de cadastro do usuario
    """
    # Atributos adicionais do formulario
    username = forms.CharField(label = "username", max_length = 250)
    email_account = forms.EmailField(label = "email_account",max_length = 150, 
                                     validators = [EmailValidator])
    password = forms.CharField(widget = forms.PasswordInput)


    class Meta:
        """
        Informacao sobre a classe a qual o formulário se refere
        """
        #tipo da classe UserInfo do arquivo FichaUsuario.models
        model = UserInfo
        fields = ['name', 'country', 'home_state_address', 'religion',
                  'civil_status', 'profession', 'gender', 'age']
    
    
    def clean(self):
        """
        Método para verificar validade de dados do usuario
        """
        cleaned_data = super(UserForm, self).clean()
        #receber nome do usuario do formulario
        username = cleaned_data.get("username")
        #receber email do formulario
        email = cleaned_data.get("email_account")
        #procurar usurio com mesmo email
        user = User.objects.filter(email = email)
        if user:
            #gerar erro
            raise forms.ValidationError("This email account already exist.")
        #procurar usuario com mesmo username
        user = User.objects.filter(username = username)
        if user:
            #gerar erro
            raise forms.ValidationError("This username account already exist.")
        return cleaned_data





class loginForm(forms.Form):
    """
    Classe de formulário que representa o login
    """
    username = forms.CharField(label = "username", max_length = 250)
    password = forms.CharField(widget = forms.PasswordInput)
