from django.db import models

# Create your models here.
from utils._base_model.base_model import BaseModel


class Develop(BaseModel):
    """发展"""

class DevelopGJ(BaseModel):
    """国家规划"""
    pass

class DevelopInternational(BaseModel):
    """国际发展"""
    pass

class DevelopBusiness(BaseModel):
    """行业发展"""
    pass