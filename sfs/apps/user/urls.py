# -*- coding: utf-8 -*-
"""
@Time    : 2021/1/17 17:04
@Author  : 半纸梁
@File    : urls.py
"""

from django.urls import path
from user import views


app_name = "user"

urlpatterns = [
    path("login/",views.RegisterView.as_view(),name="login")
]