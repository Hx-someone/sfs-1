from django.db import models

# Create your models here.
from utils._base_model.base_model import BaseModel



class Alloy(BaseModel):
    """合金统计"""
    pass

class AlloyClass(BaseModel):
    """合金分类"""
    pass

class AlloyTrait(BaseModel):
    """合金特性"""
    pass

class AlloyTackle(BaseModel):
    """合金攻关"""
    pass

