# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:44:38 2017

@author: Dylan N. Sugimoto
"""



from django.conf.urls import url
from . import views

urlpatterns = [
        # /homepage/
        #^ define o inicio
        #$ define o fim
        #^$ define a chamada padrao
        #a chamada padrao responde com a funcao index
        # a funcao index tah no arquivo views
        
        #/FichaUsuario/singUp/
        url(r"^signUp/", views.signUp.as_view(), name = "signUp"),
        #/FichaUsuario/login/
        url(r"^loginUser/", views.loginUser.as_view(), name = 'loginUser'),
        # /appname/idnumber/
        #url(r"^(?P<object_id>[0-9]+)/$", views.functionname, name = "functionname")
        #passing object_id to use as variable in functionname
        #the object_id is the idnumber from url
        ]