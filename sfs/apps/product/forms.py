# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/4 18:16
@Author  : HGhost
@File    : forms.py
"""
from django import forms
from client import models as client_model
from alloy import models as alloy_model
from craft import models as craft_model
from product import models as product_model
class ProductForm(forms.ModelForm):

    name = forms.CharField(
        label="产品名称",
        error_messages={
            "max_length": "产品名称长度不能超过32",
            "required": "产品名称不能为空"
        }
    )
    require = forms.Textarea()

    client = forms.ModelChoiceField(
        label="客户所属",
        queryset=client_model.Client.objects.only("id").filter(is_delete=False),

        error_messages={
            "required": "客户不能为空"
        }
    )
    industry = forms.ModelChoiceField(
        queryset=alloy_model.Alloy.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "合金不能为空"
        }
    )
    product_type = forms.ModelChoiceField(
        queryset=craft_model.Craft.objects.only("id").filter(is_delete=False),
        error_messages={
            "required": "工艺不能为空"
        }
    )


    class Meta:
        model = product_model.Product
        fields = ["name", "require", "client", "alloy", "craft", "remark"]
        error_messages = {
            "remark": {
                "max_length": "备注最大长度不能超过256位"
            }
        }

