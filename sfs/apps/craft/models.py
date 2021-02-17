from django.db import models
from utils._base_model.base_model import  BaseModel


class Craft(BaseModel):
    """工艺"""


    number = models.CharField(max_length=16,verbose_name="工艺编号")
    

class CraftSpecial(BaseModel):
    """特殊工艺"""
    pass

class CraftChange(BaseModel):
    """变动工艺"""
    pass

