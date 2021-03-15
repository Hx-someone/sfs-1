# from django.db import models
#
# # Create your models here.
# from utils._base_model.base_model import BaseModel
#
#
# class NationalStandard(BaseModel):
#     """国标"""
#     STANDARD_TYPE = [
#         (0,"GB"), #强制性国家标准
#         (1,"GB/T"),#推荐性国家标准
#         (2,"GB/Z"),#国家标准指导性技术文件
#         (3,"GJB"),#国军标代号
#     ]
#     number = models.CharField(max_length=32,verbose_name="国标编号")
#     name = models.CharField(max_length=256,verbose_name="国标名字")
#     using = models.CharField(max_length=256,verbose_name="国标实用方面")
#     type = models.SmallIntegerField(default=0,choices=STANDARD_TYPE,verbose_name="标准类型")
#     remark = models.CharField(max_length=256,verbose_name="备注")
#
#
#
