from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from salt import models as _models
from utils.constant import constant
from utils.page import per_page

from utils.code.json_function import to_json_data
from utils.code.res_code import Code, error_map

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

        new_salt_queryset = _models.SaltNew.objects.defer("version", "create_time", "update_time", "is_delete").filter(
            is_delete=False)
        total_data_num = len(new_salt_queryset)
        # 分页处理
        # 1.判断页码格式
        try:
            page_num = int(request.GET.get("page", 1))
        except Exception as e:
            logger.info("页码格式错误:{}".format(e))
            page_num = 1

        page_obj = Paginator(new_salt_queryset, constant.PER_PAGE_NUMBER)
        # 2.判断页码是否为空

        try:
            new_salt_info = page_obj.page(page_num)
        except Exception as e:
            new_salt_info = page_obj.page(page_obj.num_pages)

        pages_data = per_page.get_page_data(page_obj, new_salt_info)

        data = {
            "new_salt_info": new_salt_info,
            'paginator': page_obj,
            "total_data_num":total_data_num
        }

        data.update(pages_data)

        return render(request, "admin/salt/new_salt_index.html", context=data)


class SaltNewEdit(View):
    """新盐数据编辑"""

    def get(self, request, new_salt_id):
        """展示数据"""
        new_salt = _models.SaltNew.objects.filter(is_delete=False, id=new_salt_id).first()
        na_salt = _models.SaltNA.objects.filter(is_delete=False)

        if new_salt:
            return render(request, 'admin/salt/new_salt_edit.html', context={
                "data": new_salt,
                "na_query_set": na_salt
            })
        else:
            return Http404("新盐数据不存在")

    def delete(self, request, new_salt_id):
        """删除新盐检测数据"""

        new_salt = _models.SaltNew.objects.only("id").filter(is_delete=False, id=new_salt_id).first()

        if new_salt:
            new_salt.is_delete = True
            new_salt.save(update_fields=["is_delete"])
            return to_json_data(errmsg="新盐数据删除成功！")
        else:
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])

    def put(self, request, new_salt_id):
        """更新新盐检测数据"""
        new_salt = _models.SaltNew.objects.filter(is_delete=False, id=new_salt_id).first()

        if not new_salt:
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
        try:
            json_data = request.body

            if not json_data:
                return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])

            dict_data = json.loads(json_data.decode())
            _check_time = datetime.strptime(dict_data.get("check_time"), "%Y-%m-%dT%H:%M:%S.%fZ")
            dict_data["check_time"] = _check_time

            _thaw_date = datetime.strptime(dict_data.get("thaw_date"), "%Y-%m-%dT%H:%M:%S.%fZ")

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
            return to_json_data(errno=Code.UNKOWNERR, errmsg=error_map[Code.UNKOWNERR])

        # 表单校验

        form = _forms.SaltNewEditForm(dict_data)

        if form.is_valid():
            for key, value in form.cleaned_data.items():
                setattr(new_salt, key, value)
            new_salt.save()
            '2021-01-28T16:00:00.000Z'
            return to_json_data(errmsg="新盐数据更新成功")
        else:
            err_str = error_msg.err_msg_list(form)

            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)
class SaltNewAdd(View):
    def get(self,request):
        """
        新盐检测数据添加
        :param request:
        :return:
        """
        salt_na_queryset = _models.SaltNA.objects.only("id","name").filter(is_delete=False)

        return render(request,'admin/salt/new_salt_edit.html',context ={"salt_na_queryset": salt_na_queryset})
    def post(self,request):
        """
        NA 新盐数据检测添加
        :param request:
        :return:
        """
        salt_new = _models.SaltNew.objects.only("number").filter(is_delete=False)
        try:
            json_data = request.body
            if not json_data:
                return to_json_data(errno=Code.PARAMERR,errmsg=error_map[Code.PARAMERR])
            dict_data = json_data.loads(json_data.decode())

            if dict_data.name in [i.name for i in salt_new]:
                return to_json_data(errno=Code.PARAMERR,errmsg = "检测编码已存在，请重新输入!")

        except Exception as e:
            logger.info("新盐检测添加数据获取异常:{}".format(e))
            return to_json_data(errno=Code.PARAMERR,errmsg=error_map[Code.PARAMERR])
        salt_new_add_form = _forms.SaltNewEditForm(dict_data)

        if salt_new_add_form.is_valid():
            salt_new_add = salt_new_add_form.save(commit=False)
            salt_new_add.save()
            return to_json_data(errmsg="<{}>新盐数据添加成功".format(dict_data.name))

        else:
            err_str = error_msg.err_msg_list(salt_new_add_form)
            return to_json_data(errno=Code.PARAMERR,errmsg=err_str)

class SaltNAShow(View):
    """NA基盐展示和发布"""

    def get(self, request):
        """展示基盐种类"""
        salt_na = _models.SaltNA.objects.defer("version", "create_time", "update_time", "is_delete").filter(
            is_delete=False)
        total_data_num  = len(salt_na)
        try:
            page_num = int(request.Get.get("page",1))
        except Exception as e:
            logger.info("NA展示页码格式错误:{}".format(e))
            page_num = 1

        # 获取到分页对象
        page_obj = Paginator(salt_na,constant.PER_PAGE_NUMBER)

        try:
            salt_na_info = page_obj.page(page_num)
        except Exception as e:
            salt_na_info = page_obj.page(page_obj.num_pages)
        page_data  = per_page.get_page_data(page_obj,salt_na_info)

        data = {
            "salt_na_info":salt_na_info,
            "paginator":page_obj,
            "total_data_num":total_data_num
        }
        data.update(page_data)
        return render(request, "admin/salt/salt_na_index.html", context=data)

class SaltNaAdd(View):
    def get(self,request):
        """
        salt na add index
        :param request:
        :return:
        """
        return render(request,"admin/salt/salt_na_edit.html")

    def post(self,request):
        salt_na = _models.SaltNA.objects.only("name").filter()
        try:
            data = request.body
            if not data:
                return to_json_data(errno=Code.PARAMERR,errmsg=error_map[Code.PARAMERR])

            dict_data = json.loads(data.decode())

            # 判断数据库中是否已存在
            salt_sql_name = [name_query.name for name_query in salt_na]
            salt_name = dict_data.get("name")
            if salt_name in salt_sql_name:
                return to_json_data(errno=Code.PARAMERR,error_msg = "基盐已存在，请重新输入！")

        except Exception as e:
            logger.info("Salt Na 数据添加异常:{}".format(e))
            return to_json_data(errno=Code.PARAMERR,errmsg= error_map[Code.PARAMERR])

        salt_na_add_form = _forms.SaltNaEditForm(dict_data)

        if salt_na_add_form.is_valid():
            salt_na_add = salt_na_add_form.save(commit=False)
            salt_na_add.save()
            return to_json_data(error_msg="Salt Na 数据添加成功")
        else:
            err_str = error_msg.err_msg_list(salt_na_add_form)
            return to_json_data(errno=Code.PARAMERR,error_msg=err_str)

class SaltNAEdit(View):
    """NA基盐编辑"""

    def get(self, request, na_id):
        """
        NA基盐展示
        :param request:
        :param na_id:
        :return:
        """
        salt_na = _models.SaltNA.objects.filter(is_delete=False, id=na_id).first()

        return render(request, 'admin/salt/salt_na_edit.html', context={"data": salt_na})

    def delete(self, request, na_id):
        """
        NA基盐删除数据
        :param request:
        :param na_id: 基盐id
        :return:
        """
        salt_na = _models.SaltNA.objects.only("id").filter(is_delete=False, id=na_id).first()

        if salt_na:
            salt_na.is_delete = True
            salt_na.save(update_fields=["is_delete"])
            return to_json_data(errmsg="基盐数据删除成功！")
        else:
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])

    def put(self, request, na_id):

        salt_na = _models.SaltNA.objects.filter(is_delete=False, id=na_id).first()

        if not salt_na:
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])

        try:
            data = request.body
            if not data:
                return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])

            dict_data = json.loads(data.decode())
        except Exception as e:
            logger.info("基盐数据更新获取失败:{}".format(e))
            return to_json_data(errno=Code.UNKOWNERR, errmsg=error_map[Code.UNKOWNERR])

        # form表单校验
        salt_na_form = _forms.SaltNaEditForm(dict_data)

        if salt_na_form.is_valid():
            for key, value in salt_na_form.cleaned_data.items():
                setattr(salt_na, key, value)
            salt_na.save()
            return to_json_data(errmsg="基盐数据更新成功")
        else:
            err_str = error_msg.err_msg_list(salt_na_form)
            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)
