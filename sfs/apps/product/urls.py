# -*- coding: utf-8 -*-
"""
@Time    : 2021/3/28 20:31
@Author  : HGhost
@File    : urls.py
"""

from django.urls import path

from product import views

app_name = "product"
urlpatterns = [
    path("/", views.Product.as_view(), name=""),
    path("product/add/", views.ProductAdd.as_view(), name="product_add"),
    path("product/edit/<int:product_id>/", views.ProductEdit.as_view(), name="product_edit"),
]
