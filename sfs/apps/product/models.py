# from django.db import models
# from utils._base_model.base_model import BaseModel
# from client.models import  Client
# from alloy.models import  Alloy
# from craft.models import Craft
#
# class Product(BaseModel):
#     """产品"""
#     name = models.CharField(max_length=128, verbose_name="产品名字")
#     require = models.TextField(verbose_name="要求")
#     client = models.ForeignKey("Client",on_delete=models.CASCADE,verbose_name="客户")
#     alloy= models.ForeignKey("Alloy",on_delete=models.CASCADE,verbose_name="合金")
#     craft = models.ForeignKey("Craft", on_delete=models.SET_NULL,null=True,blank = True, verbose_name="工艺")
#
#
#     class Meta:
#         ordering = ["-id"]
#         db_table = "tb_product"
#         verbose_name="产品"
#         verbose_name_plural=verbose_name
#     def __str__(self):
#         return "{}的 {} 产品".format(self.client.name,self.name)