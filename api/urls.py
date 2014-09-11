# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^simple_view/', views.simple_view),
    url(r'^call_mul/', views.call_mul),
)