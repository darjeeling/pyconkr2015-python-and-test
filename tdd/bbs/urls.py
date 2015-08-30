# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, include, url

urlpatterns = patterns('bbs.views',
    #url(r'^list/$', ListView.as_view(),name="list_view"),
    #url(r'^new/$', ListView.as_view(),name="new_view"),
    #url(r'^detail/$', ListView.as_view(),name="detail_view"),
    url(r'^test/$', 'test_view' ,name="detail_view"),
)
