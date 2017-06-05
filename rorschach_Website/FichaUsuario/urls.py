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
        #/FichaUsuario/logout/
        url(r"^logout/", logout, {'next_page': "/"}, name='logout'),
        #FichaUsuario/grade/?P<string>[\w\-]+/$
        url(r"^grade/(?P<string>[\w\-]+)/$",views.SelectRandomImageView.as_view() ,name="grade"),
        #FichaUsuario/rank/?P<category>[\w\-]+/$/?P<filter>[\w\-]+/$
        url(r"^rank/?P<category>[\w\-]+/$/?P<criteria>[\w\-]+/$",views.RankView.as_view(), name = "rank"),
        ]
