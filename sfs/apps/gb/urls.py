# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/4 20:28
@Author  : HGhost
@File    : urls.py
"""

from django.urls import path
from gb import views

app_name="gb"
urlpatterns = [
    path("standard/",views.StandardShow.as_view(),name="standard"),
path("standard/add/",views.StandardAdd.as_view(),name="standard_add"),
path("standard/edit/<int:standard_id>/",views.StandardEdit.as_view(),name="standard_edit"),
]