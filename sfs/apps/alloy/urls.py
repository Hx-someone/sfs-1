# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/1 21:31
@Author  : HGhost
@File    : urls.py
"""
from django.urls import path
from alloy import views


app_name = "alloy"
urlpatterns = [
    path("alloy/",views.AlloyShow.as_view(),name="alloy"),# 合金展示
    path("alloy/add/",views.AlloyAdd.as_view(),name="alloy_add"),#合金添加
    path("alloy/edit/<int:alloy_id>/",views.AlloyEdit.as_view(),name="alloy_edit"),#合金编辑

    path("alloy/type/", views.AlloyTypeShow.as_view(), name="alloy_type"),  # 合金类型展示
    path("alloy/type/add/", views.AlloyTypeAdd.as_view(), name="alloy_type_add"),  # 合金类型添加
    path("alloy/type/edit/<int:alloy_type_id>/", views.AlloyTypeEdit.as_view(), name="alloy_type_edit"),#合金类型编辑
]