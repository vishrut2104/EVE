# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:57:40 2022

@author: ghant
"""

from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('contactus', views.contactus, name='contactus'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logind', views.logind, name='logind'),
    path('registerd', views.registerd, name='registerd'),
    path('', views.index, name='index'),
    path('addmoney', views.addmoney, name='addmoney'),
    path('addmoneyd', views.addmoneyd, name='addmoneyd'),
    path('user', views.user, name='user'),
    path('prides', views.prides, name='prides'),
    path('preports', views.preports, name='preports'),
    path('checkreports', views.preports, name='checkreports'),
    path('reportissue', views.reportissue, name='reportissue'),
    path('reportd', views.reportd, name='reportd'),
    path('viewridesm', views.viewridesm, name='viewridesm'),
    path('vieworidesm', views.vieworidesm, name='vieworidesm'),
    path('vehicles', views.vehicles, name='vehicles'),
    path('chargevehicle', views.chargevehicle, name='chargevehicle'),
    path('stations', views.stations, name='stations'),
    path('viewreportsm', views.viewreportsm, name='viewreportsm'),
    path('allpendingreports', views.allpendingreports, name='allpendingreports'),
    path('reportapprove', views.reportapprove, name='reportapprove'),
    path('reportreject', views.reportreject, name='reportreject'),
    path('reportfixed', views.reportfixed, name='reportfixed'),
    
    path('add', views.add, name='add'),
    path('addvehicletype', views.addvehicletype, name='addvehicletype'),
    path('addvehicle', views.addvehicle, name='addvehicle'),
    path('addstation', views.addstation, name='addstation'),
    
    path('addvtyped', views.addvtyped, name='addvtyped'),
    path('addvehd', views.addvehd, name='addvehd'),
    path('addstationd', views.addstationd, name='addstationd'),
    path('bookride', views.bookride, name='bookride'),
    path('bookrided', views.bookrided, name='bookrided'),
    path('bookridemain', views.bookridemain, name='bookridemain'),
    path('riding', views.riding, name='riding'),
    path('stopride', views.stopride, name='stopride'),
    
    path('getimage', views.getimage, name='getimage'),
    
    path('test', views.test, name='test'),
    path('trackride', views.trackride, name='trackride'),
    path('checkrides', views.checkrides, name='checkrides'),
    path('updateloc', views.updateloc, name='updateloc'),
    
    path('sos', views.sos, name='sos'),
    path('updatevehloc', views.updatevehloc, name='updatevehloc'),
    path('lastusers', views.lastusers, name='lastusers'),
    path('damages', views.damages, name='damages'),
    path('transactions', views.transactions, name='transactions'),
    path('paydamages', views.paydamages, name='paydamages'),
    
]