from django.shortcuts import render
from django.views import View
from alloy import models as alloy_model
from django.core.paginator import Paginator
import logging
import json
from utils.constant import constant
from utils.page import per_page
from utils.code.json_function import to_json_data
from utils.code.res_code import Code, error_map
from alloy import forms
from utils.error_select.error_msg import err_msg_list

logger = logging.getLogger("common_info")


class AlloyShow(View):
    """合金展示"""

    def get(self, request):
        """合金展示"""
        alloy_query_set = alloy_model.Alloy.objects.defer("version", "create_time", "update_time").order_by(
            "id").filter(is_delete=False)
        total_alloy = len(alloy_query_set)
        try:
            page_num = int(request.GET.get("page", 1))
        except Exception as e:
            logger.info("页码格式错误:{}".format(e))
            page_num = 1

        page_obj = Paginator(alloy_query_set, constant.PER_PAGE_NUMBER)

        try:
            alloy_info = page_obj.page(page_num)
        except Exception as e:
            logger.info("当前页面数据获取异常:{}".format(e))
            alloy_info = page_obj.page(page_obj.num_pages)
        pages_data = per_page.get_page_data(page_obj, alloy_info)
        data = {
            "alloy_info": alloy_info,
            "paginator": page_obj,
            "total_alloy": total_alloy,
        }
        data.update(pages_data)
        return render(request, 'admin/alloy/alloy_index.html', context=data)


class AlloyEdit(View):
    """合金修改"""
    def get(self, request, alloy_id):
        """
        指定合金查询展示
        :param request:
        :param alloy_id:
        :return:
        """
        alloy_type_set = alloy_model.AlloyType.objects.only("id", "type").filter(is_delete=False)
        alloy = alloy_model.Alloy.objects.only("id", "name").filter(is_delete=False, id=alloy_id)
        if alloy:
            data = {
                "alloy_type_set": alloy_type_set,
                "alloy": alloy
            }

            return render(request, 'admin/alloy/alloy_edit.html', context=data)
        else:
            logger.info("id为<{}>合金不存在".format(alloy_id))
            return to_json_data(errno=Code.PARAMERR, errmsg="id为<{}>合金不存在".format(alloy_id))

    def put(self, request, alloy_id):
        """
        指定合金修改
        :param request:
        :param alloy_id:
        :return:
        """
        alloy_query = alloy_model.Alloy.objects.only("id", "name").filter(id=alloy_id, is_delete=False)
        if not alloy_query:
            logger.info("id为<{}>合金不存在".format(alloy_id))
            return to_json_data(errno=Code.PARAMERR, errmsg="id为<{}>合金不存在".format(alloy_id))
        try:
            alloy_json_data = request.body

            if not alloy_json_data:
                logger.info("合金添加前端传来的数据为空")
                return to_json_data(errno=Code.PARAMERR, errmsg="合金添加前端传来的数据为空")
            alloy_dict_data = json.load(alloy_json_data.decode("utf-8"))
            if alloy_dict_data.get("name") in [i.name for i in alloy_query]:
                return to_json_data(errno=Code.PARAMERR, errmsg="{}合金已存在".format(alloy_dict_data.get("name")))
        except Exception as e:
            logger.info("")
            return to_json_data("")

        alloy_form = forms.AlloyForm(alloy_dict_data)
        if alloy_form.is_valid():
            for k, v in alloy_form.cleaned_data.items():
                setattr(alloy_query, k, v)
            alloy_query.save()
            return to_json_data(errmsg="<{}>合金修改成功".format(alloy_query.name))
        else:
            err_str = err_msg_list(alloy_form)

            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)

    def delete(self, request, alloy_id):
        """
        指定合金删除
        :param request:
        :param alloy_id:
        :return:
        """
        alloy = alloy_model.Alloy.objects.only("id", "name").filter(is_delete=False, id=alloy_id)
        if not alloy:
            logger.info("id为<{}>合金不存在".format(alloy_id))
            return to_json_data(errno=Code.PARAMERR, errmsg="id为<{}>合金不存在".format(alloy_id))
        else:
            alloy.is_delete = True
            alloy.update(update_fields=["is_delete"])
            alloy.save()
            return to_json_data(errmsg="<{}>合金删除成功".format(alloy.name))


class AlloyAdd(View):
    def get(self, request):
        """
        添加页面展示
        :param request:
        :return:
        """
        alloy_type_set = alloy_model.AlloyType.objects.only("id", "type").filter(is_delete=False)
        data = {
            "alloy_type_set": alloy_type_set
        }
        return render(request, 'admin/alloy/alloy_edit.html', context=data)

    def post(self, request):
        """
        新合金添加
        :param request:
        :return:
        """
        alloy_query = alloy_model.Alloy.objects.only("name").filter(is_delete=False)

        try:
            alloy_json_data = request.body

            if not alloy_json_data:
                logger.info("合金添加前端传来的数据为空")
                return to_json_data(errno=Code.PARAMERR, errmsg="合金添加前端传来的数据为空")
            alloy_dict_data = json.load(alloy_json_data.decode("utf-8"))
            if alloy_dict_data.get("name") in [i.name for i in alloy_query]:
                return to_json_data(errno=Code.PARAMERR, errmsg="{}合金已存在".format(alloy_dict_data.get("name")))
        except Exception as e:
            logger.info("")
            return to_json_data("")

        alloy_form = forms.AlloyForm(alloy_dict_data)
        if alloy_form.is_valid():
            alloy = alloy_form.save(commit=False)
            alloy.save()
        else:
            err_str = err_msg_list(alloy_form)

            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)


class AlloyTypeShow(View):
    """合金类型展示"""

    def get(self, request):
        """合金展示"""
        alloy_type_query_set = alloy_model.AlloyType.objects.defer("version", "create_time", "update_time").filter(
            is_delete=False)
        total_alloy_type = len(alloy_type_query_set)
        try:
            page_num = int(request.GET.get("page", 1))
        except Exception as e:
            logger.info("页码格式错误:{}".format(e))
            page_num = 1

        page_obj = Paginator(alloy_type_query_set, constant.PER_PAGE_NUMBER)

        try:
            alloy_type_info = page_obj.page(page_num)
        except Exception as e:
            logger.info("当前页面数据获取异常:{}".format(e))
            alloy_type_info = page_obj.page(page_obj.num_pages)
        pages_data = per_page.get_page_data(page_obj, alloy_type_info)
        data = {
            "alloy_type_info": alloy_type_info,
            "paginator": page_obj,
            "total_alloy_type": total_alloy_type,
        }
        data.update(pages_data)
        return render(request, 'admin/alloy/alloy_type_index.html', context=data)


class AlloyTypeEdit(View):
    """合金类型修改"""

    def get(self, request, alloy_type_id):
        """
        指定合金类型查询展示
        :param request:
        :param alloy_type_id:
        :return:
        """

        alloy_type = alloy_model.AlloyType.objects.only("id", "type").filter(is_delete=False, id=alloy_type_id)
        if alloy_type:
            data = {
                "alloy_type": alloy_type,
            }

            return render(request, 'admin/alloy/alloy_type_edit.html', context=data)
        else:
            logger.info("id为<{}>合金类型不存在".format(alloy_type_id))
            return to_json_data(errno=Code.PARAMERR, errmsg="id为<{}>合金类型不存在".format(alloy_type_id))

    def put(self, request, alloy_type_id):
        """
        指定合金类型修改
        :param request:
        :param alloy_type_id:
        :return:
        """
        alloy_type_query = alloy_model.Alloy.objects.only("id", "type").filter(id=alloy_type_id, is_delete=False)
        if not alloy_type_query:
            logger.info("id为<{}>合金类型不存在".format(alloy_type_id))
            return to_json_data(errno=Code.PARAMERR, errmsg="id为<{}>合金类型不存在".format(alloy_type_id))
        try:
            alloy_type_json_data = request.body

            if not alloy_type_json_data:
                logger.info("合金添加前端传来的数据为空")
                return to_json_data(errno=Code.PARAMERR, errmsg="合金添加前端传来的数据为空")
            alloy_type_dict_data = json.load(alloy_type_json_data.decode("utf-8"))
            if alloy_type_dict_data.get("type") in [i.type for i in alloy_type_query]:
                return to_json_data(errno=Code.PARAMERR, errmsg="{}合金类型已存在".format(alloy_type_dict_data.get("type")))
        except Exception as e:
            logger.info("")
            return to_json_data("")

        alloy_type_form = forms.AlloyTypeForm(alloy_type_dict_data)
        if alloy_type_form.is_valid():
            for k, v in alloy_type_form.cleaned_data.items():
                setattr(alloy_type_query, k, v)
            alloy_type_query.save()
            return to_json_data(errmsg="<{}>合金修改成功".format(alloy_type_query.type))
        else:
            err_str = err_msg_list(alloy_type_form)

            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)

    def delete(self, request, alloy_type_id):
        """
        指定合金删除
        :param request:
        :param alloy_type_id:
        :return:
        """
        alloy_type = alloy_model.Alloy.objects.only("id", "type").filter(is_delete=False, id=alloy_type_id)
        if not alloy_type:
            logger.info("id为<{}>合金类型不存在".format(alloy_type_id))
            return to_json_data(errno=Code.PARAMERR, errmsg="id为<{}>合金类型不存在".format(alloy_type_id))
        else:
            alloy_type.is_delete = True
            alloy_type.update(update_fields=["is_delete"])
            alloy_type.save()
            return to_json_data(errmsg="<{}>合金类型删除成功".format(alloy_type.type))


class AlloyTypeAdd(View):
    def get(self, request):
        """
        添加页面展示
        :param request:
        :return:
        """

        return render(request, 'admin/alloy/alloy_type_edit.html')

    def post(self, request):
        """
        新合金类型添加
        :param request:
        :return:
        """
        alloy_type_query = alloy_model.AlloyType.objects.only("type").filter(is_delete=False)

        try:
            alloy_type_json_data = request.body

            if not alloy_type_json_data:
                logger.info("合金添加前端传来的数据为空")
                return to_json_data(errno=Code.PARAMERR, errmsg="合金添加前端传来的数据为空")
            alloy_type_dict_data = json.load(alloy_type_json_data.decode("utf-8"))
            if alloy_type_dict_data.get("type") in [i.type for i in alloy_type_query]:
                return to_json_data(errno=Code.PARAMERR, errmsg="{}合金已存在".format(alloy_type_dict_data.get("name")))
        except Exception as e:
            logger.info("")
            return to_json_data("")

        alloy_type_form = forms.AlloyForm(alloy_type_dict_data)
        if alloy_type_form.is_valid():
            alloy_type = alloy_type_form.save(commit=False)
            alloy_type.save()
        else:
            err_str = err_msg_list(alloy_type_form)

            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)

