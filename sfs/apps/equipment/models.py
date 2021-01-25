from django.db import models

# Create your models here.
from utils._base_model.base_model import BaseModel

processes = [
    (0, "抛光"),
    (1, "超声"),
    (2, "预热"),
    (3, "氮化"),
    (4, "氧化"),
    (5, "乳化"),
    (6, "封闭"),
    (7, "包装"),
    (8, "清洗")

]
idle = [
    (0, "闲置"),
    (1, "正常生产"),
    (2, "报废")
]


class Equipment(BaseModel):
    """设备"""
    number = models.CharField(max_length=14, verbose_name="设备编号")
    name = models.CharField(max_length=32, verbose_name="设备名称")
    process = models.SmallIntegerField(default=3, choices=processes, verbose_name="工序")
    size = models.CharField(max_length=32, verbose_name="设备尺寸")
    power = models.CharField(max_length=16, verbose_name="功耗")
    materials = models.CharField(max_length=16, verbose_name="材料")
    is_idle = models.SmallIntegerField(default=1, choices=idle, verbose_name="设备状态")
    buy_time = models.DateField(verbose_name="购买时间")

    # examine = models.ForeignKey()

    class Meta:
        ordering = ["-number", "-id"]
        db_table = "tb_equipment"
        verbose_name = "设备管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
