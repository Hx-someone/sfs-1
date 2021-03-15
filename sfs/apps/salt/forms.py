# -*- coding: utf-8 -*-
"""
@Time    : 2021/3/7 22:54
@Author  : HGhost
@File    : forms.py
"""

from django import forms
from django.core.validators import RegexValidator
from salt import models as _models


class SaltNewEditForm(forms.ModelForm):
    check_time = forms.DateField(label="检测时间", error_messages={"required": "检测时间格式不能为空"})
    stove_number = forms.IntegerField(
        label="炉号",
        error_messages={
            "required": "炉号不能为空"
        }
    )

    number = forms.CharField(
        label="编号",

        error_messages={
            "max_length":"编号长度不是14位",
            "min_length": "编号长度不是14位",
            "required": "编号不能为空"
        }
    )


    salt_na = forms.ModelChoiceField(
        queryset=_models.SaltNA.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "盐 类不能为空"
        }
    )
    team = forms.IntegerField(label="化盐班组")
    inspector = forms.IntegerField(label="检测人员")
    thaw_date = forms.DateField(label="检测时间", error_messages={"required": "检测时间格式不能为空"})



    class Meta:
        model = _models.SaltNew
        fields = ["check_time","stove_number","number","salt_na","thaw_date","team","inspector","remark"]

        error_messages={
            "remark":{
                "max_length":"备注长度不能超过256"
            }
        }
