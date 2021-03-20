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
            "max_length": "编号长度不是14位",
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
        fields = ["check_time", "stove_number", "number", "salt_na", "thaw_date", "team", "inspector", "remark"]

        error_messages = {
            "remark": {
                "max_length": "备注长度不能超过256"
            }
        }


class SaltNaEditForm(forms.ModelForm):
    name = forms.CharField(label="基盐名字",
                           error_messages={
                               "max_length": "基盐名字长度太长",
                               "required": "名字不能为空"
                           })
    type = forms.CharField(label="基盐类型",
                           error_messages={
                               "max_length":"基盐类型名字太长",
                               "required":"基盐类型不能为空"
                           })
    new_salt_thaw_craft = forms.CharField(label="基盐融化工艺",
                           error_messages={
                               "max_length":"基盐融化工艺太长",
                               "required":"基盐融化不能为空"
                           })
    using_salt_thaw_craft = forms.CharField(label="基盐使用工艺",
                                          error_messages={
                                              "max_length": "基盐使用工艺太长",
                                              "required": "基盐使用工艺不能为空"
                                          })
    apply_alloy = forms.CharField(label="基盐实用合金",
                                            error_messages={
                                                "max_length": "基盐实用合金太长",
                                                "required": "基盐实用合金不能为空"
                                            })

    trait = forms.CharField(label="特性",
                                  error_messages={
                                      "max_length": "特性字符太长",
                                      "required": "特性字符不能为空"
                                  })

    class Meta:
        model = _models.SaltNA
        fields = ["name","type","new_salt_thaw_craft","using_salt_thaw_craft","apply_alloy","trait","remark"]

        error_messages = {
            "remark": {
                "max_length": "备注长度不能超过256"
            }
        }