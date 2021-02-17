# -*- coding: utf-8 -*-
"""
@Time    : 2021/1/28 22:00
@Author  : 半纸梁
@File    : forms.py
"""
import re
from django import forms
from django.contrib.auth import login

from user.models import Users
from utils.constant import constant


class LoginForm(forms.Form):
    user_name = forms.CharField(
        max_length=18,
        min_length=5,

        error_messages={
            "max_length": "用户名格式不正确",
            "min_length": "用户名格式不正确",
            "required": "用户名不能为空"
        }

    )
    password = forms.CharField(
        max_length=18,
        min_length=6,
        error_messages={
            "max_length": "密码格式不正确",
            "min_length": "密码格式不正确",
            "required": "密码不能为空"
        }
    )

    remember = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_user_name(self):

        user_name = self.cleaned_data.get("user_name")

        if not user_name:
            raise forms.ValidationError("登录名为空")

        if not len(user_name) < 5 or len(user_name) > 18:
            raise forms.ValidationError("登录名格式不正确")

        return user_name

    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get("user_name")
        password = self.cleaned_data.get("password")
        remember_me = cleaned_data.get("remember")

        user_queryset = Users.objects.filter(user_name=user_name)

        if user_queryset:
            user = user_queryset.first()

            if user.check_password(password):
                if remember_me:
                    self.request.session.set_expiry(constant.SESSION_EXPIRY_TIME)  # 设置过期时间
                else:
                    self.request.session.set_expiry(0)

                login(self.request, user)
            else:
                raise forms.ValidationError("密码不正确，请重新输入")
        else:
            raise forms.ValidationError("用户不存在，请重新输入")
