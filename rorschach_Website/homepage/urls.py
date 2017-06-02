# -*- coding: utf-8 -*-
"""
Created on Sat May 27 20:07:10 2017

@author: Dylan N. Sugimoto
"""

from django.conf.urls import url, include
from . import views

urlpatterns = [
        # /homepage/
        #^ define o inicio
        #$ define o fim
        #^$ define a chamada padrao
        #a chamada padrao responde com a funcao index
        # a funcao index tah no arquivo views
        url(r"^$", views.index, name = "index"),
        url(r"^loginUser/", include("FichaUsuario.urls")),
        url(r"^signUp/", include("FichaUsuario.urls")),
        url(r"^perfil/", views.perfil, name = "perfil"),
        # /appname/idnumber/
        #url(r"^(?P<object_id>[0-9]+)/$", views.functionname, name = "functionname")
        #passing object_id to use as variable in functionname
        
        ]