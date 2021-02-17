from django.db import models
from utils._base_model import base_model


# Create your models here.

class Users(base_model.BaseModel):
    user_name = models.CharField(
        verbose_name="用户名",
        min_length=5,
        max_length=18,
        unique = True,
        error_messages={
            "unique":"用户名已被注册"
        }
    )
    password = models.CharField(verbose_name="密码", min_length=5, max_length=18)



    class Meta:
        ordering = ["update_time","id"]
        db_table = "tb_users"
        verbose_name ="用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name