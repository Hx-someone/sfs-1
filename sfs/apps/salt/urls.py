# -*- coding: utf-8 -*-
"""
@Time    : 2020/11/23 10:05
@Author  : 半纸梁
@File    : urls.py
"""
from django.urls import path
from salt import views
app_name = "salt"
urlpatterns = [
    path("new/",views.SaltNewShow.as_view(),name = "new"),
    path("new/edit/<int:new_salt_id>/",views.SaltNewEdit.as_view(),name = "new_salt_edit"),

]