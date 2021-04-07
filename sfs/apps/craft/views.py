from django.shortcuts import render

from django.views import View
from craft import models
from utils.constant import constant
from utils.error_select import error_msg
from utils.models_common import view_model
from utils.code.res_code import Code, error_map
from utils.code.json_function import to_json_data
from django.core.paginator import Paginator

from client import models as client_model
from alloy import models as alloy_model

from craft import forms

from utils.page import per_page
import json
import logging
logger = logging.getLogger('common_info')

class CraftShow(View):
    def get(self,request):
        craft_queryset = models.Craft.objects.defer("version", "create_time", "update_time", "is_delete").filter(
            is_delete=False)
        total_data_num = len(craft_queryset)
        # 分页处理
        # 1.判断页码格式
        try:
            page_num = int(request.GET.get("page", 1))
        except Exception as e:
            logger.info("页码格式错误:{}".format(e))
            page_num = 1

        page_obj = Paginator(craft_queryset, constant.PER_PAGE_NUMBER)
        # 2.判断页码是否为空

        try:
            craft_info = page_obj.page(page_num)
        except Exception as e:
            logger.info("当前页数据获取异常:{}".format(e))
            craft_info = page_obj.page(page_obj.num_pages)

        pages_data = per_page.get_page_data(page_obj, craft_info)

        data = {
            "craft_info": craft_info,
            'paginator': page_obj,
            "total_data_num": total_data_num
        }

        data.update(pages_data)

        return render(request, "admin/craft/craft_index.html", context=data)

class CraftEdit(View):
    def get(self, request, craft_id):
        """展示数据"""
        craft_query = models.Craft.objects.filter(is_delete=False, id=craft_id).first()
        craft_special_queryset = view_model.view_common(models.CraftSpecial, "id", "name")
        client_queryset = view_model.view_common(client_model.Client, "id", "name")
        alloy_queryset = view_model.view_common(alloy_model.Alloy, "id", "name")

        if craft_query:
            return render(request, 'admin/salt/salt_new_edit.html', context={
                "craft_query": craft_query,
                "craft_special_queryset": craft_special_queryset,
                "client_queryset": client_queryset,
                "alloy_queryset": alloy_queryset,

            })
        else:
            return to_json_data(errno=Code.PARAMERR, errmsg="id为<{}>工艺不存在".format(craft_id))
    def put(self,request,craft_id):
        craft_query = models.Craft.objects.only("id").filter(
            is_delete=False, id=craft_id).first()

        if not craft_query:
            return to_json_data(errno=Code.PARAMERR, errmsg="id为{}的工艺不存在".format(craft_id))
        try:
            craft_json_data = request.body

            if not craft_json_data:
                return to_json_data(errno=Code.PARAMERR, errmsg="工艺更新前端传来数据为空")
            craft_dict_data = json.loads(craft_json_data.decode("utf-8"))
        except Exception as e:
            logger.info("工艺更新数据获取异常:{}".format(e))
            return to_json_data(errno=Code.PARAMERR, errmsg="设备更新数据获取异常:{}".format(e))
        craft_put_form = forms.CraftForm(craft_dict_data)

        if craft_put_form.is_valid():
            for key, value in craft_put_form.cleaned_data.items():
                setattr(craft_query, key, value)
            craft_query.save()
            return to_json_data(errmsg="工艺编号为:<{}>工艺更新更新成功".format(craft_query.number))

        else:
            err_str = error_msg.err_msg_list(craft_put_form)
            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)
    def delete(self,request,craft_id):
        craft_query = models.Craft.objects.only("id","number").filter(is_delete=False,
                                                                                 id=craft_id).first()

        if craft_query:
            craft_query.is_delete = True
            craft_query.save(update_fields=["is_delete"])
            return to_json_data(errmsg="工艺信息删除成功！")
        else:
            return to_json_data(errno=Code.PARAMERR, errmsg="id为{}的工艺不存在".format(craft_id))
class CraftAdd(View):
    def get(self, request):
        craft_special_queryset = view_model.view_common(models.CraftSpecial, "id", "name")
        client_queryset = view_model.view_common(client_model.Client, "id", "name")
        alloy_queryset = view_model.view_common(alloy_model.Alloy, "id", "name")
        data = {
            "craft_special_queryset": craft_special_queryset,
            "client_queryset": client_queryset,
            "alloy_queryset": alloy_queryset
        }
        return render(request, 'admin/craft/craft_edit.html', context=data)

    def post(self, request):
        craft_queryset = models.Craft.objects.defer("version", "create_time", "update_time").filter(
            is_delete=False)

        try:
            craft_json_data = request.body

            if not craft_json_data:
                return to_json_data(errno=Code.PARAMERR, errmsg="工艺添加前端传来数据为空")
            craft_dict_data = json.loads(craft_json_data.decode("utf-8"))

            if craft_dict_data["number"] in [i.number for i in craft_queryset]:
                return to_json_data(errno=Code.PARAMERR, errmsg="工艺编号已存在，请重新输入!")

        except Exception as e:
            logger.info("工艺添加数据获取异常:{}".format(e))
            return to_json_data(errno=Code.PARAMERR, errmsg="工艺添加数据获取异常:{}".format(e))
        craft_add_form = forms.CraftForm(craft_dict_data)

        if craft_add_form.is_valid():
            craft_add = craft_add_form.save(commit=False)
            craft_add.save()
            return to_json_data(errmsg="编号为<{}>工艺添加成功".format(craft_dict_data["number"]))

        else:
            err_str = error_msg.err_msg_list(craft_add_form)
            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)

class CraftSpecialShow(View):
    def get(self,request):
        craft_special_queryset = models.CraftSpecial.objects.defer("version", "create_time", "update_time",
                                                            "is_delete").filter(
            is_delete=False)
        total_data_num = len(craft_special_queryset)
        # 分页处理
        # 1.判断页码格式
        try:
            page_num = int(request.GET.get("page", 1))
        except Exception as e:
            logger.info("页码格式错误:{}".format(e))
            page_num = 1

        page_obj = Paginator(craft_special_queryset, constant.PER_PAGE_NUMBER)
        # 2.判断页码是否为空

        try:
            craft_special_info = page_obj.page(page_num)
        except Exception as e:
            logger.info("当前页数据获取异常:{}".format(e))
            craft_special_info = page_obj.page(page_obj.num_pages)

        pages_data = per_page.get_page_data(page_obj, craft_special_info)

        data = {
            "craft_special_info": craft_special_info,
            'paginator': page_obj,
            "total_data_num": total_data_num
        }

        data.update(pages_data)

        return render(request, "admin/craft/craft_special_index.html", context=data)
class CraftSpecialEdit(View):
    def get(self, request, craft_special_id):
        """展示数据"""
        craft_special_query = models.CraftSpecial.objects.only("id","name").filter(is_delete=False,
                                                                            id=craft_special_id).first()


        if craft_special_query:
            return render(request, 'admin/craft/craft_special_edit.html', context=craft_special_query)
        else:
            return to_json_data(errno=Code.PARAMERR, errmsg="id为<{}>特殊工艺不存在".format(craft_special_id))

    def put(self, request, craft_special_id):
        craft_special_query = models.CraftSpecial.objects.only("id").filter(
            is_delete=False, id=craft_special_id).first()

        if not craft_special_query:
            return to_json_data(errno=Code.PARAMERR, errmsg="id为{}特殊工艺不存在".format(craft_special_id))
        try:
            craft_special_json_data = request.body

            if not craft_special_json_data:
                return to_json_data(errno=Code.PARAMERR, errmsg="特殊工艺更新前端传来数据为空")
            craft_special_dict_data = json.loads(craft_special_json_data.decode("utf-8"))
        except Exception as e:
            logger.info("特殊工艺更新数据获取异常:{}".format(e))
            return to_json_data(errno=Code.PARAMERR, errmsg="特殊工艺更新数据获取异常:{}".format(e))
        craft_special_put_form = forms.CraftForm(craft_special_dict_data)

        if craft_special_put_form.is_valid():
            for key, value in craft_special_put_form.cleaned_data.items():
                setattr(craft_special_query, key, value)
                craft_special_query.save()
            return to_json_data(errmsg="名称为:<{}>特殊工艺更新更新成功".format(craft_special_query.name))

        else:
            err_str = error_msg.err_msg_list(craft_special_put_form)
            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)

    def delete(self, request, craft_special_id):
        craft_special_query = models.CraftSpecial.objects.only("id", "name").filter(is_delete=False,
                                                                       id=craft_special_id).first()

        if craft_special_query:
            craft_special_query.is_delete = True
            craft_special_query.save(update_fields=["is_delete"])
            return to_json_data(errmsg="特殊工艺信息删除成功！")
        else:
            return to_json_data(errno=Code.PARAMERR, errmsg="id为{}的特殊工艺不存在".format(craft_special_id))


class CraftSpecialAdd(View):
    def get(self, request):

        return render(request, 'admin/craft/craft_special_edit.html')

    def post(self, request):
        craft_special_queryset = models.CraftSpecial.objects.defer("version", "create_time", "update_time").filter(
            is_delete=False)

        try:
            craft_special_json_data = request.body

            if not craft_special_json_data:
                return to_json_data(errno=Code.PARAMERR, errmsg="特殊工艺添加前端传来数据为空")
            craft_special_dict_data = json.loads(craft_special_json_data.decode("utf-8"))

            if craft_special_dict_data["name"] in [i.name for i in craft_special_queryset]:
                return to_json_data(errno=Code.PARAMERR, errmsg="特殊工艺<{}>已存在，请重新输入!".format(craft_special_dict_data["name"]))

        except Exception as e:
            logger.info("特殊工艺添加数据获取异常:{}".format(e))
            return to_json_data(errno=Code.PARAMERR, errmsg="特殊工艺添加数据获取异常:{}".format(e))
        craft_special_add_form = forms.CraftForm(craft_special_dict_data)

        if craft_special_add_form.is_valid():
            craft_special_add = craft_special_add_form.save(commit=False)
            craft_special_add.save()
            return to_json_data(errmsg="名称为<{}>特殊工艺添加成功".format(craft_special_dict_data["name"]))

        else:
            err_str = error_msg.err_msg_list(craft_special_add_form)
            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)