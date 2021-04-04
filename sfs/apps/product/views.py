# from django.shortcuts import render
#
# # Create your views here.
# from django.views import View
# from product import models
# from utils.code.res_code import Code, error_map
# from utils.code.json_function import to_json_data
# from django.core.paginator import Paginator
# from utils.constant import constant
# from utils.page import per_page
# import logging
# from client import models as client_model
# from alloy import models as alloy_model
# from craft import models as craft_model
# from utils.models_common import view_model
# import json
# from product import forms
# from utils.error_select import error_msg
#
# logger = logging.getLogger("common_info")
#
#
# class Product(View):
#     """产品展示"""
#
#     def get(self, request):
#         product_query_set = models.Product.objects.defer("version", "create_time", "update_time").filter(
#             is_delete=False)
#
#         total_product = len(product_query_set)
#         try:
#             page_num = request.GET.get("page", 1)
#
#         except Exception as e:
#             page_num = 1
#
#         page_obj = Paginator(product_query_set, constant.PER_PAGE_NUMBER)  # 获取到整个数据对象
#         try:
#             product_info = page_obj.page(page_num)  # 获取到需要获取的页码的数据
#         except Exception as e:
#             product_info = page_obj.get_page(page_obj.num_pages)
#         pages_data = per_page.get_page_data(page_obj, product_info)
#
#         data = {
#             "total_product": total_product,
#             "page_obj": page_obj,
#             "product_info": product_info,
#         }
#         data.update(pages_data)
#         return render(request, 'admin/product/product_index.html', context=data)
#
#
# class ProductEdit(View):
#     """产品修改"""
#
#     def get(self, request, product_id):
#         product_query = models.Product.objects.only("id", "name").filter(is_delete=False, id=product_id).first()
#         if not product_query:
#             logger.info("{}的产品不存在".format(product_id))
#             return to_json_data(errno=Code.PARAMERR, errmsg="{}的产品不存在".format(product_id))
#         client_query_set = view_model.view_common(client_model.Client, "id", "name")
#         alloy_query_set = view_model.view_common(alloy_model.Alloy, "id", "name")
#         craft_query_set = view_model.view_common(craft_model.Craft, "id", "name")
#
#         data = {
#             "product_query": product_query,
#             "client_query_set": client_query_set,
#             "alloy_query_set": alloy_query_set,
#             "craft_query_set": craft_query_set,
#         }
#
#         return render(request, 'admin/product/product_index.html', context=data)
#
#     def delete(self, request, product_id):
#         product_query = models.Product.objects.only("id", "name").filter(is_delete=False, id=product_id).first()
#         if not product_query:
#             logger.info("{}的产品不存在".format(product_id))
#             return to_json_data(errno=Code.PARAMERR, errmsg="{}的产品不存在".format(product_id))
#         product_query.is_delete = True
#         product_query.update(update_fields=["is_delete"])
#         product_query.save()
#         return to_json_data(errmsg="{}产品删除成功".format(product_query.name))
#
#     def put(self, request, product_id):
#         product_query = models.Product.objects.only("id", "name").filter(is_delete=False, id=product_id).first()
#         if not product_query:
#             logger.info("{}的产品不存在".format(product_id))
#             return to_json_data(errno=Code.PARAMERR, errmsg="{}的产品不存在".format(product_query))
#         try:
#             product_json_data = request.body
#             if not product_json_data:
#                 return to_json_data(errno=Code.PARAMERR, errmsg="产品更新前端传递数据为空")
#             product_dict_data = json.load(product_json_data.decode("utf-8"))
#         except  Exception as e:
#             logger.info("{}的产品不存在".format(product_id))
#             return to_json_data(errno=Code.PARAMERR, errmsg="{}的产品不存在".format(product_query))
#
#         product_form = forms.ProductForm(product_dict_data)
#
#         if product_form.is_valid():
#             for k, v in product_form.cleaned_data.items():
#                 setattr(product_query, k, v)
#             product_query.save()
#             return to_json_data(errmsg="{}产品更新成功".format(product_query.name))
#         else:
#             err_str = error_msg.err_msg_list(product_form)
#             return to_json_data(errno=Code.PARAMERR, errmsg=err_str)
#
#
# class ProductAdd(View):
#     """产品增加"""
#
#     def get(self, request):
#         client_query_set = view_model.view_common(client_model.Client, "id", "name")
#         alloy_query_set = view_model.view_common(alloy_model.Alloy, "id", "name")
#         craft_query_set = view_model.view_common(craft_model.Craft, "id", "name")
#         data = {
#             "client_query_set": client_query_set,
#             "alloy_query_set": alloy_query_set,
#             "craft_query_set": craft_query_set,
#         }
#         return render(request, 'admin/product/product_edit.html', context=data)
#
#     def post(self, request):
#         try:
#             product_json_data = request.body
#             if not product_json_data:
#                 return to_json_data(errno=Code.PARAMERR, errmsg="产品更新前端传递数据为空")
#             product_dict_data = json.load(product_json_data.decode("utf-8"))
#         except  Exception as e:
#             logger.info("产品添加前端传递数据异常:{}".format(e))
#             return to_json_data(errno=Code.PARAMERR, errmsg="产品添加前端传递数据异常:{}".format(e))
#
#         product_form = forms.ProductForm(product_dict_data)
#
#         if product_form.is_valid():
#             product = product_form.save(commit=False)
#             product.save()
#             return to_json_data(errmsg="{}-{}产品添加成功".format(product_dict_data.get("client")["name"],
#                                                             product_dict_data.get(
#                                                                 "name")))
#         else:
#             err_str = error_msg.err_msg_list(product_form)
#             return to_json_data(errno=Code.PARAMERR, errmsg=err_str)
