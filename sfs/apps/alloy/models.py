# from django.db import models
#
# # Create your models here.
# from utils._base_model.base_model import BaseModel
#
#
#
# class Alloy(BaseModel):
#     """合金统计"""
#     name = models.CharField(max_length=16,verbose_name="合金牌号")
#     standard = models.CharField(max_length=16,verbose_name="牌号标准")
#     type = models.CharField(max_length=32, verbose_name="合金种类")
#     special = models.CharField(max_length=256,verbose_name ="合金特性")
#     common_craft = models.CharField(max_length=32,verbose_name="正常工艺")
#     special_craft = models.CharField(max_length = 32,verbose_name="特殊工艺")
#     tackle = models.CharField(max_length = 64,verbose_name="攻关")
#     remark = models.CharField(max_length = 256,verbose_name="备注")
#
#
#     class Meta:
#         ordering = ["name","-id"]
#         db_table = "tb_alloy"
#         verbose_name = "合金统计"
#         verbose_name_plural = verbose_name
#
#
#     def __str__(self):
#
#         return self.name
