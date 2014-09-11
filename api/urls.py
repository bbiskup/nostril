# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from .views import simple_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^simple_view/', simple_view),
)