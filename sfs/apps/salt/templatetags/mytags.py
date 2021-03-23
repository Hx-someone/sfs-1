# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/24 23:29
@Author  : HGhost
@File    : mytags.py
"""

from django import template
from datetime import datetime

register = template.Library()


@register.filter(name="team_choice")
def team_choice(value):
    """转换化盐班组"""
    if value:
        return "X"
    else:
        return "L"
@register.filter(name="inspector_choice")
def inspector_choice(value):
    if value:
        return "T"
    else:
        return "H"

@register.filter(name="date_str")
def date_format(_date):
    """

    :param _date:  日期格式
    :return:
    """
    return datetime.strftime(_date,"%Y-%m-%d")
