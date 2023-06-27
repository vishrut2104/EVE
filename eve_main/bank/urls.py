# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 08:52:28 2022

@author: ghant
"""

from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('approve', views.approve, name='approve'),
    path('reject', views.reject, name='reject'),
]