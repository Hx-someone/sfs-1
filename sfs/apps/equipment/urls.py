# -*- coding: utf-8 -*-
"""
@Time    : 2020/11/23 10:05
@Author  : 半纸梁
@File    : urls.py
"""
from django.urls import path
from equipment import views

app_name = "equipment"
urlpatterns = [
    path("equipment/", views.EquipmentShow.as_view(), name="equipment"),
    path("equipment/add/", views.EquipmentAdd.as_view(), name="equipment_add"),
    path("equipment/edit/<int:equipment_id>/", views.EquipmentEdit.as_view(), name="equipment_edit"),
]
