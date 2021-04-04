# -*- coding: utf-8 -*-
"""
@Time    : 2021/3/28 22:17
@Author  : HGhost
@File    : forms.py
"""

from django import forms
from client import models as client_models


class ClientForm(forms.ModelForm):
    """客户form校验"""

    number = forms.CharField(
        label="客户编号",
        error_messages={
            "max_length": "客户编号长度不能超过8",
            "required": "客户编号不能为空"
        }
    )
    name = forms.CharField(
        label="客户名字",
        error_messages={
            "max_length": "客户名字长度不能超过32",
            "required": "客户名字不能为空"
        }
    )
    abbr = forms.CharField(
        label="客户简介",
        error_messages={
            "max_length": "客户简介长度不能超过64",
        }
    )
    address = forms.CharField(
        label="客户地址",
        error_messages={
            "max_length": "客户地址长度不能超过256",
        }
    )
    belong = forms.ModelChoiceField(
        label="客户所属",
        queryset=client_models.ClientBelong.objects.only("id").filter(is_delete=False),

        error_messages={
            "required": "客户所属不能为空"
        }
    )
    industry = forms.ModelChoiceField(
        queryset=client_models.ClientIndustry.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "客户性质不能为空"
        }
    )
    product_type = forms.ModelChoiceField(
        queryset=client_models.ClientProductType.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "产品行业不能为空"
        }
    )
    mark = forms.ModelChoiceField(
        queryset=client_models.ClientMark.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "客户等级不能为空"
        }
    )
    type = forms.ModelChoiceField(
        queryset=client_models.ClientType.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "客户类型不能为空"
        }
    )

    class Meta:
        model = client_models.Client
        fields = ["number", "name", "abbr", "address", "belong", "industry", "product_type", "mark", "type","remark"]
        error_messages = {
            "remark": {
                "max_length": "备注最大长度不能超过256位"
            }
        }

