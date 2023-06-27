# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:57:40 2022

@author: ghant
"""

from django.urls import path
from . import views

urlpatterns = [
    path('trackride', views.trackride, name='trackride'),
    path('getloc', views.getloc, name='getloc'),
    
]