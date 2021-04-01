from django.db import models

# Create your models here.
from utils._base_model.base_model import BaseModel


class Alloy(BaseModel):
    """合金统计"""
    name = models.CharField(max_length=16,verbose_name="合金牌号")
    type = models.ForeignKey("AlloyType",on_delete =models.SET_NULL,null=True,blank=True,verbose_name="合金种类")
    tackle = models.CharField(max_length = 256,verbose_name="攻关")
    class Meta:
        db_table = "tb_alloy"
        verbose_name = "合金"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class AlloyType(BaseModel):
    """合金类型"""
    type = models.CharField(max_length=256,verbose_name="合金类型")

    class Meta:
        db_table = "tb_alloy_type"
        verbose_name = "合金类型"
        verbose_name_plural = verbose_name
