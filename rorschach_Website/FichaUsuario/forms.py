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
    #classe que representa o formulario de cadastro do usuario
    #atributos do formulario
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
#------------------------------------Fim dos atributos-------------------------
    class Meta:
        #informacao sobre a classe
        #tipo da classe UserInfo do arquivo FichaUsuario.models
        model = UserInfo
        #definir os atributos do objeto que sera criado com este formulario
        fields = ['name','username', 'email_account', 'password', 'country', 
                  'home_state_adress', 'religion','civil_status', 'profession',
                  'gender', 'age']
    def clean(self):
        #metodo para verificar validade de dados do usuario
        cleaned_data = super(UserForm,self).clean()
        #receber nome do usuario do formulario
        username = cleaned_data.get("username")
        #receber email do formulario
        email = cleaned_data.get("email_account")
        #procurar usurio com mesmo email
        user = UserInfo.objects.filter(email_account = email)
        if user:
            #gerar erro
            print("error2")
            print(user)
            raise forms.ValidationError("This email account already exist.")
        #procurar usuario com mesmo username
        user = UserInfo.objects.filter(username = username)
        if user:
            #gerar erro
            print("error username exist")
            print(user)
            raise forms.ValidationError("This username account already exist.")
        return cleaned_data


class loginForm(forms.ModelForm):
    #classe que representa o login
    #atributos da classe
    password = forms.CharField(widget = forms.PasswordInput)
    login = forms.CharField(label = "login", max_length = 150)
#-------------------------------Fim dos atributos------------------------------
    class Meta:
        #informacoes sobre do objeto a ser criado a partir deste formulario
        #tipo User
        model = User
        #atributos do objeto
        fields = ['login', 'password']