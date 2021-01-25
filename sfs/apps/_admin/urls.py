# -*- coding: utf-8 -*-
"""
@Time    : 2020/11/23 10:32
@Author  : 半纸梁
@File    : urls.py
"""
from django.urls import path
from _admin import views
app_name = "_admin"
urlpatterns = [

    path("index/",views.ShowIndex.as_view(),name="index")
]