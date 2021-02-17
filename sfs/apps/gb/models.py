from django.db import models

# Create your models here.
from utils._base_model.base_model import BaseModel


class GBSaltBath(BaseModel):
    """盐浴国标"""
    pass

class GBTexture(BaseModel):
    """材质国标"""
    pass

class GBOther(BaseModel):
    """其他国标"""
    pass