# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/4 22:18
@Author  : HGhost
@File    : urls.py
"""
from django.urls import path
from craft import views

app_name = "craft"
urlpatterns = [
    path("craft/",views.CraftShow.as_view(),name="craft"),
path("craft/add/",views.CraftAdd.as_view(),name="craft_add"),
path("craft/edit/<int:craft_id>/",views.CraftEdit.as_view(),name="craft_edit"),

path("craft/special/",views.CraftSpecialShow.as_view(),name="craft_special"),
path("craft/special/add/",views.CraftSpecialAdd.as_view(),name="craft_special_add"),
path("craft/special/edit/<int:craft_special_id>/",views.CraftSpecialEdit.as_view(),name="craft_special_edit"),
]