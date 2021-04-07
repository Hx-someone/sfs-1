from django.shortcuts import render

# Create your views here.
import json
from django.views import View
from equipment import models
from equipment import forms
from utils.models_common import view_model
from utils.code.res_code import Code, error_map
from utils.code.json_function import to_json_data
from utils.error_select.error_msg import  err_msg_list
import logging

logger = logging.getLogger("common_info")


class EquipmentShow(View):
    """设备展示"""

    def get(self, request):
        equipment_query_set = models.Equipment.objects.defer("version", "create_time", "update_time").filter(
            is_delete=False)

        return render(request, 'admin/equipment/equipment_index.html', context=equipment_query_set)


class EquipmentAdd(View):
    """设备添加"""
    def get(self, request):
        process_query_set = view_model.view_common(models.Processes, "id", "process")
        idle_query_set = view_model.view_common(models.Idle, "id", "status")
        data = {
            "process_query_set": process_query_set,
            "idle_query_set": idle_query_set
        }
        return render(request, 'admin/equipment/equipment_edit.html', context=data)

    def post(self, request):
        equipment_query_set = models.Equipment.objects.defer("version", "create_time", "update_time").filter(
            is_delete=False)

        try:
            equipment_json_data = request.body

            if not equipment_json_data:
                return to_json_data(errno=Code.PARAMERR, errmsg="设备添加前端传来数据为空")
            equipment_dict_data = json.loads(equipment_json_data.decode("utf-8"))

            if equipment_dict_data["number"] in [i.number for i in equipment_query_set]:
                return to_json_data(errno=Code.PARAMERR, errmsg="设备编号已存在，请重新输入!")

        except Exception as e:
            logger.info("设备添加数据获取异常:{}".format(e))
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
        equipment_add_form = forms.EquipmentForm(equipment_dict_data)

        if equipment_add_form.is_valid():
            equipment_add = equipment_add_form.save(commit=False)
            equipment_add.save()
            return to_json_data(errmsg="编号为<{}>设备添加成功".format(equipment_dict_data["number"]))

        else:
            err_str = err_msg_list(equipment_add_form)
            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)



class EquipmentEdit(View):
    def get(self, request, equipment_id):
        equipment_query_set = models.Equipment.objects.only("id").filter(
            is_delete=False, id=equipment_id)

        if not equipment_query_set:
            return to_json_data(errno=Code.PARAMERR, errmsg="id为{}的设备不存在".format(equipment_id))
        process_query_set = view_model.view_common(models.Processes, "id", "process")
        idle_query_set = view_model.view_common(models.Idle, "id", "status")
        data = {
            "equipment_query_set": equipment_query_set,
            "process_query_set": process_query_set,
            "idle_query_set": idle_query_set
        }
        return render(request, 'admin/equipment/equipment_edit.html', context=data)

    def delete(self, request, equipment_id):
        equipment = models.Equipment.objects.only("id","name","number").filter(is_delete=False, id=equipment_id).first()

        if equipment:
            equipment.is_delete = True
            equipment.save(update_fields=["is_delete"])
            return to_json_data(errmsg="设备信息删除成功！")
        else:
            return to_json_data(errno=Code.PARAMERR, errmsg="id为{}的设备不存在".format(equipment_id))

    def put(self, request, equipment_id):
        equipment_query= models.Equipment.objects.only("id").filter(
            is_delete=False, id=equipment_id).first()

        if not equipment_query:
            return to_json_data(errno=Code.PARAMERR, errmsg="id为{}的设备不存在".format(equipment_id))
        try:
            equipment_json_data = request.body

            if not equipment_json_data:
                return to_json_data(errno=Code.PARAMERR, errmsg="设备更新前端传来数据为空")
            equipment_dict_data = json.loads(equipment_json_data.decode("utf-8"))
        except Exception as e:
            logger.info("设备更新数据获取异常:{}".format(e))
            return to_json_data(errno=Code.PARAMERR, errmsg="设备更新数据获取异常:{}".format(e))
        equipment_put_form = forms.EquipmentForm(equipment_dict_data)

        if equipment_put_form.is_valid():
            for key, value in equipment_put_form.cleaned_data.items():
                setattr(equipment_query, key, value)
            equipment_query.save()
            return to_json_data(errmsg="<{}>设备更新更新成功".format(equipment_query.name))

        else:
            err_str = err_msg_list(equipment_put_form)
            return to_json_data(errno=Code.PARAMERR, errmsg=err_str)