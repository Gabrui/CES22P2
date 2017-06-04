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
        #url para direcionar para o perfil, executar metodo views.perfil
        url(r"^perfil/(?P<pk>[0-9]+)/$", 
            views.PerfilView.as_view(),
            name = "perfil"),
        #/homepage/myaccount
        url(r"^(?P<pk>[0-9]+)/myAccount/",views.UpdateAccount.as_view(success_url='perfil'),name ="myAccount"),
        #/homepage/addAlbum namespace = addAlbum
        url(r"^album/add/$", views.AlbumAdder.as_view(), name="addAlbum"),
        #/homepage/album namespace = album
        url(r"^album/(?P<pk>[0-9]+)/$",
            views.AlbumDetailView.as_view(),name = "album")
        ]