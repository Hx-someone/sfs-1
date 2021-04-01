# -*- coding: utf-8 -*-
"""
@Time    : 2021/3/28 23:39
@Author  : HGhost
@File    : forms.py
"""

from django import forms
from alloy.models import AlloyType

class AlloyForm(forms.Form):
    """合金表单校验"""
    name = forms.CharField(label="合金牌号",error_messages={
        "max_length":"合金牌号长度不能超过16位",
        "required":"合金牌号不能为空"
    })
    type = forms.ModelChoiceField(
        queryset = AlloyType.objects.only("id").filter(is_delete=False),
    error_messages = {
        "required": "类型不能为空"
    }
    )
    tackle = forms.CharField(label="攻关",error_messages={
        "max_length":"攻关长度不能超过256位"
    })
class AlloyTypeForm(forms.Form):
    """合金类型表单校验"""
    name = forms.CharField(label="合金类型", error_messages={
        "max_length": "合金类型长度不能超过256位"
    })