from django.shortcuts import render

# Create your views here.
from django.views import View
from gb import models
from utils.models_common import view_model
from utils.code import res_code
from utils.code import json_function
import logging
import json
from gb import forms
from utils.error_select.error_msg import  err_msg_list

logger = logging.getLogger("common_info")

class StandardShow(View):
    def get(self,request):
        standard_query_set =models.NationalStandard.objects.defer("version","update_time","create_time").filter(
            is_delete=False)
        return render(request,'admin/gb/gb_index.html',context=standard_query_set)
class StandardEdit(View):
    def get(self,request,standard_id):
        standard_query= models.NationalStandard.objects.only("id").filter(
            is_delete=False,id=standard_id)

        if not standard_query:
            logger.info("国标更新异常：不存在该国标")
            return json_function.to_json_data(errno=res_code.Code.PARAMERR,errmsg="国标更新异常：不存在该国标")
        standard_type_query = view_model.view_common(models.StandardType,"id","name")
        data = {
            "standard_query":standard_query,
            "standard_type_query": standard_type_query,
        }
        return render(request,'admin/gb/gb_edit.html',context=data)
    def delete(self,request,standard_id):
        standard_query = models.NationalStandard.objects.only("id","is_delete","name").filter(
            is_delete=False, id=standard_id)

        if not standard_query:
            logger.info("国标更新异常：不存在该国标")
            return json_function.to_json_data(errno=res_code.Code.PARAMERR, errmsg="国标更新异常：不存在该国标")
        standard_query.is_delete = True
        standard_query.update(update_fields =["is_delete"])
        standard_query.save()
        return json_function.to_json_data(errmsg="{}国标更新成功".format(standard_query.name))
    def put(self,request,standard_id):
        standard_query = models.NationalStandard.objects.only("id", "is_delete", "name").filter(
            is_delete=False, id=standard_id)

        if not standard_query:
            logger.info("国标更新异常：不存在该国标")
            return json_function.to_json_data(errno=res_code.Code.PARAMERR, errmsg="国标更新异常：不存在该国标")

        try:
            standard_json_data = request.body
            if not standard_json_data:
                return json_function.to_json_data(errno=res_code.Code.PARAMERR, errmsg="国标更新：前端传来的数据为空")
            standard_dict_data = json.load(standard_json_data.decode("utf-8"))
        except Exception as e:
            logger.info("国标更新异常:{}".format(e))
            return json_function.to_json_data(errno=res_code.Code.PARAMERR, errmsg="国标更新异常:{}".format(e))
        standard_form = forms.StandardForm(standard_dict_data)
        if standard_form.is_valid():
            for k,v in standard_form.cleaned_data.items():
                setattr(models.NationalStandard,k,v)
            standard_query.save()
            return json_function.to_json_data(errmsg="{}国标更新成功".format(standard_query.name))
        else:
            standard_form_err = err_msg_list(standard_form)
            return json_function.to_json_data(errno=res_code.Code.PARAMERR, errmsg=standard_form_err)

class StandardAdd(View):
    def get(self,request):
        standard_type_query = view_model.view_common(models.StandardType, "id", "name")
        data = {
            "standard_type_query": standard_type_query,
        }
        return render(request, 'admin/gb/gb_edit.html', context=data)
    def post(self,request):
        try:
            standard_json_data = request.body
            if not standard_json_data:
                return json_function.to_json_data(errno=res_code.Code.PARAMERR, errmsg="国标添加:前端传来的数据为空")
            standard_dict_data = json.load(standard_json_data.decode("utf-8"))
        except Exception as e:
            logger.info("国标添加异常:{}".format(e))
            return json_function.to_json_data(errno=res_code.Code.PARAMERR, errmsg="国标添加异常:{}".format(e))
        standard_form = forms.StandardForm(standard_dict_data)
        if standard_form.is_valid():
            standard =  standard_form.save(commit=False)
            standard.save()
            return json_function.to_json_data(errmsg="{}国标添加成功".format(standard_dict_data.get("name")))
        else:
            standard_form_err = err_msg_list(standard_form)
            return json_function.to_json_data(errno=res_code.Code.PARAMERR, errmsg=standard_form_err)
