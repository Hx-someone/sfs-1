from django.db import models

# Create your models here.
from utils._base_model.base_model import BaseModel


class NationalStandard(BaseModel):
    """国标"""
    number = models.CharField(max_length=32,verbose_name="国标编号")
    name = models.CharField(max_length=256,verbose_name="国标名字")
    using = models.CharField(max_length=256,verbose_name="国标实用方面")
    type = models.ForeignKey("StandardType",on_delete=models.SET_NULL,null=True,blank=True)


    class Meta:
        ordering = ["-id"]
        db_table = "tb_Standard_national"
        verbose_name = "标准"
        verbose_name_plural = verbose_name


    def __str__(self):
        return "标准为:{}".format(self.name)



   # STANDARD_TYPE = [
   #      (0,"GB"), #强制性国家标准
   #      (1,"GB/T"),#推荐性国家标准
   #      (2,"GB/Z"),#国家标准指导性技术文件
   #      (3,"GJB"),#国军标代号
   #  ]
class StandardType(BaseModel):
    """标准类型"""
    name = models.CharField(max_length=32,verbose_name="标准类型",unique=True)

    class Meta:
        ordering=["-id"]
        db_table="tb_standard_type"
        verbose_name="标准类型"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "标准类型为:{}".format(self.name)