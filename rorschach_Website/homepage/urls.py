# -*- coding: utf-8 -*-
"""
Created on Sat May 27 20:07:10 2017

@author: Dylan N. Sugimoto
"""

from django.conf.urls import url
from . import views

urlpatterns = [
        
        url(r"^$", views.index, name = "index"),
        
        
        ]