# -*- coding: utf-8 -*-
"""
@Time    : 2020/11/23 10:05
@Author  : 半纸梁
@File    : urls.py
"""
from django.urls import path
from client import views

app_name = "client"

urlpatterns = [
    path("index/",views.ShowIndex.as_view(),name="index")
]