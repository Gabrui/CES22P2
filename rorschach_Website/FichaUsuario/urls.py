# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:44:38 2017

@author: Dylan N. Sugimoto
"""



from django.conf.urls import url
from django.conf import settings
from . import views
from django.contrib.auth.views import logout

app_name = "FichaUsuario"

urlpatterns = [
        # /homepage/
        #^ define o inicio
        #$ define o fim
        #^$ define a chamada padrao
        #a chamada padrao responde com a funcao index
        # a funcao index tah no arquivo views
        
        #/FichaUsuario/singUp/
        #url para tratar o cadastro do usuario, executar os metodos da classe singUp
        url(r"^signUp/", views.signUp.as_view(), name = "signUp"),
        #/FichaUsuario/login/
        #url para tratar o login do usuario, executar os metodos da classe login
        url(r"^loginUser/", views.loginUser.as_view(), name = 'loginUser'),
        url(r"^logOut/", logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
        # /appname/idnumber/
        #url(r"^(?P<object_id>[0-9]+)/$", views.functionname, name = "functionname")
        #passing object_id to use as variable in functionname
        #the object_id is the idnumber from url
        ]