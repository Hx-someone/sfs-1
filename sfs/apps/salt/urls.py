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
    path("new/", views.SaltNewShow.as_view(), name="new"),
    path("new/add/", views.SaltNewAdd.as_view(), name="salt_new_add"),
    path("new/edit/<int:salt_new_id>/", views.SaltNewEdit.as_view(), name="salt_new_edit"),

    path("na/", views.SaltNAShow.as_view(), name="na"),
    path("na/add/", views.SaltNaAdd.as_view(), name="salt_na_add"),
    path("na/edit/<int:salt_na_id>/", views.SaltNAEdit.as_view(), name="salt_na_edit"),

    path("daily/", views.SaltDailyShow.as_view(), name="daily"),
    path("daily/add/", views.SaltDailyAdd.as_view(), name="salt_daily_add"),
    path("daily/edit/<int:salt_daily_id>/", views.SaltDailyEdit.as_view(), name="salt_daily_edit"),

]
