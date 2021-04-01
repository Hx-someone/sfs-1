from django.shortcuts import render
from client import models
import json

from django.views import View
import logging
from django.core.paginator import  Paginator
from utils.constant import constant
from utils.page import per_page
from utils.models_common import view_model
from utils.code.json_function import to_json_data
from utils.code.res_code import Code,error_map
from client.forms import ClientForm
from utils.error_select.error_msg import err_msg_list

logger = logging.getLogger("common_info")

class ClientShow(View):
    """
    show index
    """

    def get(self,request):
        """展示客户信息界面"""
        client_query_set = models.Client.objects.defer("create_time","update_time","version").filter(is_delete =False)
        total_client = len(client_query_set)
        try:
            page_num =int(request.GET.get("page",1))
        except Exception as e:
            logger.info("客户页码展示错误:{}".format(e))
            page_num = 1

        page_obj  = Paginator(client_query_set,constant.PER_PAGE_NUMBER)

        try:
            client_info = page_obj.page(page_num)
        except Exception as e:
            logger.info("当前页码不存在:{}".format(e))
            client_info = page_obj.page(page_obj.num_pages)

        pages_data = per_page.get_page_data(page_obj,client_info)
        data = {
            "client_info":client_info,
            "paginator":page_obj,
            "total_client":total_client
        }
        data.update(pages_data)


        return render(request,"admin/client/index.html",context =data)
class ClientEdit(View):
    """客户编辑"""
    def get(self,request,client_id):
        client_query  = models.Client.objects.only("id").filter(is_delete=False,id=client_id).first()
        if not client_query:
            logger.info("id为{}的客户不存在".format(client_id))
            return to_json_data(errno=Code.PARAMERR,errmsg = "id为{}的客户不存在".format(client_id))

        client_belong_query_set = view_model.view_common(models.ClientBelong,"id","belong")
        client_product_type_query_set = view_model.view_common(models.ClientProductType, "id", "type")
        client_industry_query_set = view_model.view_common(models.ClientIndustry, "id", "industry")
        client_type_query_set = view_model.view_common(models.ClientType, "id", "type")
        client_mark_query_set = view_model.view_common(models.ClientMark, "id", "mark")

        data = {
            "client_query":client_query,
            "client_belong_query_set": client_belong_query_set,
            "client_product_type_query_set": client_product_type_query_set,
            "client_industry_query_set": client_industry_query_set,
            "client_type_query_set": client_type_query_set,
            "client_mark_query_set": client_mark_query_set,
        }

        return render(request,"admin/client/client_edit.html",context=data)
    def delete(self,request,client_id):
        client_query = models.Client.objects.only("id","name").filter(is_delete=False, id=client_id).first()
        if not client_query:
            logger.info("id为{}的客户不存在".format(client_id))
            return to_json_data(errno=Code.PARAMERR, errmsg="id为{}的客户不存在".format(client_id))
        client_query.is_delete = True
        client_query.save(update_fields=["is_delete"])

        return to_json_data(errmsg="<{}>客户成功删除".foramt(client_query.name))


    def put(self,request,client_id):
        client_query = models.Client.objects.only("id","name").filter(is_delete=False, id=client_id).first()
        if not client_query:
            logger.info("id为{}的客户不存在".format(client_id))
            return to_json_data(errno=Code.PARAMERR, errmsg="id为{}的客户不存在".format(client_id))

        try:
            client_json_data = request.body
            if not client_json_data:
                logger.info("{}修改数据传递为空".format(client_query.name))
                return to_json_data(errno=Code.PARAMERR, errmsg="{}修改数据传递为空".format(client_query.name))
            client_dict_data = json.loads(client_json_data.decode("utf-8"))
        except Exception as e:
            logger.info("前端数据传递异常:{}".format(e))
            return to_json_data(errno=Code.PARAMERR, errmsg="前端数据传递异常:{}".format(e))

        client_form = ClientForm(client_dict_data)
        if client_form.is_valid():
            for k,v in client_form.cleaned_data.items():
                setattr(client_query,k,v)
            client_query.save()
            return to_json_data(errmsg="客户更新成功".format(client_query.name))
        else:
            err_str = err_msg_list(client_form)
            return to_json_data(errno=Code.PARAMERR,errmsg=err_str)


class ClientAdd(View):
    """客户增加"""
    def get(self,request):
        client_belong_query_set = view_model.view_common(models.ClientBelong, "id", "belong")
        client_product_type_query_set = view_model.view_common(models.ClientProductType, "id", "type")
        client_industry_query_set = view_model.view_common(models.ClientIndustry, "id", "industry")
        client_type_query_set = view_model.view_common(models.ClientType, "id", "type")
        client_mark_query_set = view_model.view_common(models.ClientMark, "id", "mark")

        data = {
            "client_belong_query_set": client_belong_query_set,
            "client_product_type_query_set": client_product_type_query_set,
            "client_industry_query_set": client_industry_query_set,
            "client_type_query_set": client_type_query_set,
            "client_mark_query_set": client_mark_query_set,
        }
        return render(request,'admin/client/client_edit.html',context=data)
    def post(self,request):
        client_query_set = models.Client.objects.only("name").filter(is_delete=False)


        try:
            client_json_data = request.body
            if not client_json_data:
                logger.info("客户添加数据传递为空")
                return to_json_data(errno=Code.PARAMERR, errmsg="客户添加数据传递为空")
            client_dict_data = json.loads(client_json_data.decode("utf-8"))
        except Exception as e:
            logger.info("前端数据传递异常:{}".format(e))
            return to_json_data(errno=Code.PARAMERR, errmsg="前端数据传递异常:{}".format(e))
        if client_dict_data.get("name") in [i.name for i in client_query_set]:
            logger.info("{}客户已存在，请重新输入！".format(client_dict_data.get("name")))
            return to_json_data(errno=Code.PARAMERR, errmsg="{}客户已存在".format(client_dict_data.get("name")))

        client_form = ClientForm(client_dict_data)
        if client_form.is_valid():
            client_add = client_form.save(commit=False)
            client_add.save()
            return to_json_data(errmsg="{}客户添加成功".format(client_dict_data.get("name")))
        else:
            err_str = err_msg_list(client_form)
            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)
