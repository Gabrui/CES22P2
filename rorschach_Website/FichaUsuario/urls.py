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
        url(r"^$", views.index, name = "index"),
        url(r"^SingUp/$", views.singup.as_view(), name = "singup"),
        # /appname/idnumber/
        #url(r"^(?P<object_id>[0-9]+)/$", views.functionname, name = "functionname")
        #passing object_id to use as variable in functionname
        
        ]