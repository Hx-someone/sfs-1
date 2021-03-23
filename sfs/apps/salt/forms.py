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
    """
    salt new form
    """
    number = forms.CharField(
        label="编号",
        error_messages={
            "max_length": "编号长度不是14位",
            "min_length": "编号长度不是14位",
            "required": "编号不能为空"
        }
    )
    cn = forms.DecimalField(label="氰根")
    co3 = forms.DecimalField(label="碳酸根")
    cno = forms.DecimalField(label="氰酸根")
    thaw_date = forms.DateField(label="检测时间", error_messages={"required": "检测时间格式不能为空"})
    check_time = forms.DateField(label="检测时间", error_messages={"required": "检测时间格式不能为空"})
    batch = forms.CharField(
        label="批号",
        error_messages={
            "max_length": "编号长度超过10位"
        }
    )
    inspector = forms.ModelChoiceField(
        queryset=_models.Inspector.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "盐检测人不能为空"
        }
    )
    salt_na = forms.ModelChoiceField(
        queryset=_models.SaltNA.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "盐 类不能为空"
        }
    )
    stove_number = forms.ModelChoiceField(
        queryset= _models.StoveNumber.objects.only("id").filter(is_delete=False),
        error_messages = {
            "required": "盐 类不能为空"
        }
    )
    team = forms.ModelChoiceField(
        queryset=_models.Team.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "班组不能为空"
        }
    )



    class Meta:
        model = _models.SaltNew
        fields = ["check_time", "stove_number", "number", "salt_na", "thaw_date", "team", "inspector", "remark","cn",
                  "co3","cno","batch"]

        error_messages = {
            "remark":{
                "max_length":"最大长度不能超过256位"
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


class SaltDailyForm(forms.ModelForm):
    """炉盐检测表单校验"""
    number = forms.CharField(
        label = "检测编码",
        error_messages={
            "max_length":"检测编码长度不能超过14",
            "min_length": "检测编码长度不能低于14",
            "required":"检测编码不能为空"
        }
    )
    cn = forms.DecimalField(
        label="氰根",
        error_messages={
            "max_digits": "氰根位数不能超过5位",
            "decimal_places": "氰根小数点位数为3",
        }
    )
    co3 = forms.DecimalField(
        label="碳酸根",
        error_messages={
            "max_digits": "碳酸根位数不能超过5位",
            "decimal_places": "碳酸根小数点位数为3",
        }
    )
    cno = forms.DecimalField(
        label="氰酸根",
        error_messages={
            "max_digits": "氰酸根位数不能超过5位",
            "decimal_places": "氰酸根小数点位数为3",
        }
    )
    check_time = forms.DateField(label="检测时间", error_messages={"required": "检测时间格式不能为空"})
    stove_number = forms.ModelChoiceField(
        query = _models.StoveNumber.objects.only("id").filter(is_delete=False),
        error_messages={
            "required":"炉号不能为空"
        }
    )
    status = forms.ModelChoiceField(
        query=_models.SaltStatus.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "炉盐状态不能为空"
        }
    )
    salt_na = forms.ModelChoiceField(
        query=_models.SaltNA.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "NA种类不能为空"
        }
    )
    inspector = forms.ModelChoiceField(
        query=_models.Inspector.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "检测人不能为空"
        }
    )

    class Meta:
        model = _models.SaltCheck
        fields = ["number", "cn", "co3", "cno", "check_time", "stove_number", "status","salt_na","inspector","remark"]
        error_messages = {
            "remark":{
                "max_length":"备注最大长度不能超过256位"
            }
        }