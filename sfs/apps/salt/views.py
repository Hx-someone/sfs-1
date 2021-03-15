from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from salt import models as _models
from utils.constant import constant
from utils.page import per_page

from utils.code.json_function import to_json_data
from utils.code.res_code import Code,error_map

from django.http.response import Http404

from salt import forms as _forms
from utils.error_select import error_msg
import logging
import json

from datetime import datetime

logger = logging.getLogger('common_info')
class SaltNewShow(View):
    """新盐检测数据"""

    def get(self, request):
        """获取数据展示数据"""

        new_salt_queryset= _models.SaltNew.objects.defer("version", "create_time", "update_time", "is_delete").filter(
            is_delete=False)

        # 分页处理
        # 1.判断页码格式
        try:
            page_num = int(request.GET.get("page",1))
        except Exception as e:
            logger.info("页码格式错误:{}".format(e))
            page_num = 1

        page_obj = Paginator(new_salt_queryset, constant.PER_PAGE_NUMBER)
        # 2.判断页码是否为空

        try:
            new_salt_info = page_obj.page(page_num)
        except Exception as e:
            new_salt_info = page_obj.page(page_obj.num_pages)

        pages_data = per_page.get_page_data(page_obj,new_salt_info)

        data = {
            "new_salt_info":new_salt_info,
            'paginator':page_obj,
        }

        data.update(pages_data)

        return render(request, "admin/salt/new_salt_index.html", context=data)

    def post(self):
        pass
class SaltNewEdit(View):
    """新盐数据编辑"""

    def get(self,request,new_salt_id):
        """展示数据"""
        new_salt = _models.SaltNew.objects.filter(is_delete=False,id=new_salt_id).first()
        na_salt = _models.SaltNA.objects.filter(is_delete =False)

        if new_salt:
            return render(request,'admin/salt/new_salt_edit.html',context={
                "data":new_salt,
                "na_query_set":na_salt
            })
        else:
            return Http404("新盐数据不存在")


    def delete(self,request,new_salt_id):
        """删除新盐检测数据"""

        new_salt = _models.SaltNew.objects.only("id").filter(is_delete=False,id=new_salt_id).first()

        if new_salt:
            new_salt.is_delete = True
            new_salt.save(update_fields=["is_delete"])
            return to_json_data(errmsg="新盐数据删除成功！")
        else:
            return to_json_data(errno=Code.PARAMERR,errmsg=error_map[Code.PARAMERR])


    def put(self,request,new_salt_id):
        """更新新盐检测数据"""
        new_salt = _models.SaltNew.objects.filter(is_delete=False,id=new_salt_id).first()

        if not new_salt:
            return to_json_data(errno=Code.PARAMERR,errmsg=error_map[Code.PARAMERR])
        try:
            json_data = request.body

            if not json_data:
                return to_json_data(errno=Code.PARAMERR,errmsg=error_map[Code.PARAMERR])


            dict_data = json.loads(json_data.decode())
            _check_time = datetime.strptime(dict_data.get("check_time"),"%Y-%m-%dT%H:%M:%S.%fZ")
            dict_data["check_time"] =_check_time

            _thaw_date = datetime.strptime(dict_data.get("thaw_date"),"%Y-%m-%dT%H:%M:%S.%fZ")

            dict_data["thaw_date"] = _thaw_date

            team = dict_data.get("team")
            if team == "L":
                team = 0
            else:
                team = 1
            dict_data["team"] = team
            inspector = dict_data.get("inspector")
            if inspector == "H":
                inspector = 1
            else:
                inspector = 0
            dict_data["inspector"] = inspector

        except Exception as e:
            logger.info("新盐数据更新获取失败:{}".format(e))
            return to_json_data(errno=Code.UNKOWNERR,errmsg=error_map[Code.UNKOWNERR])

            # 表单校验
        print(dict_data)
        form = _forms.SaltNewEditForm(dict_data)

        if form.is_valid():
            for key,value in form.cleaned_data.items():
                setattr(new_salt,key,value)
            new_salt.save()
            '2021-01-28T16:00:00.000Z'
            return to_json_data(errmsg="新盐数据更新成功")
        else:
            err_str = error_msg.err_msg_list(form)


            return to_json_data(errno=Code.PARAMERR,errmsg=err_str)


class SaltNAShow(View):
    """NA基盐"""

    def get(self,request):
        """展示基盐种类"""
        salt_na = _models.SaltNA.objects.defer("version","create_time", "update_time", "is_delete").filter(
            is_delete=False)

        return render(request,"admin/salt/salt_na_index.html",locals())