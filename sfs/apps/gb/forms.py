# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/4 20:44
@Author  : HGhost
@File    : forms.py
"""
from gb import models

from django import forms

class StandardForm(forms.ModelForm):
    number = forms.CharField(
        label="国标编号",
        error_messages={
            "max_length": "国标编号长度不能超过32",
            "required": "国标编号不能为空"
        }
    )
    name = forms.CharField(
        label="国标名字",
        error_messages={
            "max_length": "国标名字长度不能超过256",
            "required": "国标名字不能为空"
        }
    )
    using = forms.CharField(
        label="国标实用方面",
        error_messages={
            "max_length": "国标实用方面长度不能超过256"

        }
    )
    mark = forms.ModelChoiceField(
        queryset=models.StandardType.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "国标类型等级不能为空"
        }
    )


    class Meta:
        model = models.NationalStandard
        fields = ["number", "name", "using", "type","remark"]
        error_messages = {
            "remark": {
                "max_length": "备注最大长度不能超过256位"
            }
        }
