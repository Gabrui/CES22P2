# -*- coding: utf-8 -*-
"""
Created on Sat May 27 20:07:10 2017

@author: Dylan N. Sugimoto
"""

from django.conf.urls import url, include
from . import views

app_name = "homepage"

urlpatterns = [
        # /homepage/
        #^ define o inicio
        #$ define o fim
        #^$ define a chamada padrao
        #a chamada padrao responde com a funcao index
        # a funcao index tah no arquivo views
        url(r"^$",
            views.SendTemplateView.as_view(template_name = "homepage/homepage.html"),
            name = "index"),
        #url para tratar do login, olhar na urls do app FichaUsuario
        url(r"^loginUser/", include("FichaUsuario.urls")),
        #url para tratar do cadastro, olhar na urls do app FicaUsuario
        url(r"^signUp/", include("FichaUsuario.urls")),
        #url para direcionar para o perfil, executar metodo views.perfil
        url(r"^perfil/(?P<pk>[0-9]+)/$", 
            views.PerfilView.as_view(),
            name = "perfil"),
        url(r"^myAccount/(?P<pk>[0-9]+)/",views.UpdateAccount.as_view(),name ="myAccount"),
        
        ]