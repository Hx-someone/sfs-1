from django.db import models
from utils._base_model.base_model import  BaseModel
# from client.models import Client
# from alloy.models import Alloy


class Craft(BaseModel):
    """工艺"""
    number = models.CharField(max_length=16,verbose_name="工艺编号")
    ultrasound = models.CharField(max_length=64,verbose_name="超声清洗")
    preheat = models.CharField(max_length=64,verbose_name="预热")
    nitriding = models.CharField(max_length=32,verbose_name="氮化")
    oxidation = models.CharField(max_length=32, verbose_name="氧化")
    hardening = models.CharField(max_length=32, verbose_name="淬水")
    cold_rinse= models.CharField(max_length=32, verbose_name="冷水清洗")
    hot_rinse = models.CharField(max_length=32, verbose_name="热水清洗")
    emulsify = models.CharField(max_length=64, verbose_name="乳化")
    close = models.CharField(max_length=32, verbose_name="封闭")
    client = models.ForeignKey("Client",on_delete=models.CASCADE,verbose_name="客户")
    alloy = models.ForeignKey("Alloy",on_delete=models.SET_NULL,null=True,blank=True,verbose_name="合金")
    special = models.ForeignKey("CraftSpecial", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="特殊工艺")

    class Meta:
        db_table = "tb_craft"
        verbose_name = "工艺"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.alloy.name

class CraftSpecial(BaseModel):
    """特殊工艺"""
    shot = models.CharField(max_length=32,verbose_name="抛光")
    second_preheat = models.CharField(max_length=64,verbose_name="二次预热")
    second_oxidation = models.CharField(max_length=32,verbose_name="二次氧化")
    second_hardening = models.CharField(max_length=32, verbose_name="淬水")
    second_cold_rinse = models.CharField(max_length=32, verbose_name="冷水清洗")
    second_hot_rinse = models.CharField(max_length=32, verbose_name="热水清洗")
    second_shot = models.CharField(max_length=32, verbose_name="二次抛光",default="")
    emulsify = models.CharField(max_length=64, verbose_name="乳化")
    close = models.CharField(max_length=32, verbose_name="封闭")

    class Meta:
        db_table = "tb_craft_special"
        verbose_name = "工艺"
        verbose_name_plural = verbose_name





