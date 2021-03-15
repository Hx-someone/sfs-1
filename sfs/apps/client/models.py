# from django.db import models
# from utils._base_model import base_model
# from alloy.models import Alloy
#
#
# class Client(base_model.BaseModel):
#     """客户"""
#     vip_mark = [
#         (0, "VIP1"),
#         (1, "VIP2"),
#         (2, "VIP3"),
#         (3, "VIP4"),
#         (4, "VIP5"),
#         (5, "VIP6"),
#     ]
#
#     client_kinds = [
#         (0, "加工"),
#         (1, "盐"),
#         (2, "设备"),
#         (3, "自动化")
#     ]
#     number = models.CharField(max_length=8, verbose_name="客户编号", help_text="客户编号")
#     name = models.CharField(max_length=32, verbose_name="客户名称", help_text="客户名称")
#     abbr = models.CharField(max_length=64, verbose_name="客户简介", help_text="客户简介")
#     address = models.CharField(max_length=256, verbose_name="客户地址", help_text="客户地址")
#     belong = models.CharField(max_length=8, verbose_name="客户所属", help_text="客户所属")  # 属于哪个销售人员
#     industry = models.CharField(max_length=16, verbose_name="所属行业", help_text="所属行业")  # 属于什么行业
#     vip = models.SmallIntegerField(default=5, choices=vip_mark, verbose_name="客户等级", help_text="客户等级")
#     kind = models.SmallIntegerField(default=0, choices=client_kinds, verbose_name="客户类型", help_text="客户类型")
#
#     class Meta:
#         ordering = ["-vip", "-id"]
#         db_table = "tb_client"
#         verbose_name = "客户"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         """
#         展示客户名称
#         :return:
#         """
#         return self.name
# class ClientDetail(base_model.BaseModel):
#     """客户产品相关"""
#     alloy = models.ForeignKey("Alloy",on_delete=models.SET_NULL,null=True,blank=True)  # 关联合金
#
#
#
#
# class ClientProblem(base_model.BaseModel):
#     """"客户产品问题"""
#     pass
#
# class ClientComplaint(base_model.BaseModel):
#     """客户投诉"""
#     pass
#
# class ClientDifficult(base_model.BaseModel):
#     """客户难点异常"""
#     pass
