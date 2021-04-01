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
    path("client/",views.ClientShow.as_view(),name="client"),
    path("client/add/",views.ClientAdd.as_view(),name="client_add"),
    path("client/edit/<int:client_id>/",views.ClientEdit.as_view(),name="client_edit"),
]