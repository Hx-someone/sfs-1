from django.db import models

from utils._base_model.base_model import BaseModel

kinds = [
    (0, "随炉"),
    (1, "在线产品"),
    (2, "新产品试制"),
    (3, "客户来样"),
]

n_number = [
    (0, "外来"),
    (1, "1#"),
    (2, "2#"),
    (3, "3#"),
    (4, "4#"),
    (5, "小试验炉"),
    (6, "大试验炉")

]


class Metal(BaseModel):
    """金相"""

    number = models.CharField(max_length=8, verbose_name="金相编号")
    kind = models.SmallIntegerField(default=0, choices=kinds, verbose_name="金相类型")
    name = models.CharField(max_length=32, verbose_name="产品名称")
    n_number = models.SmallIntegerField(default=1, choices=n_number, verbose_name="炉号")
    batch = models.CharField(max_length=8, verbose_name="批号")
    time = models.CharField(max_length=5, verbose_name="出炉时间")
    craft = models.CharField(max_length=16, verbose_name="工艺")
    image = models.URLField(default="", verbose_name="金相图片")
    core_hardness = models.IntegerField(verbose_name="芯部硬度")
    _2_hardness = models.IntegerField(verbose_name="0.2mm处硬度")
    _5_hardness = models.IntegerField(verbose_name="0.5mm处硬度")
    surface_hardness = models.IntegerField(verbose_name="表面硬度")
    total_deep = models.DecimalField(verbose_name="总渗层")
    compound_layer = models.IntegerField(verbose_name="化合物层")
    rank = models.SmallIntegerField(verbose_name="级别")
    check_time = models.DateField(verbose_name="检测时间")
    material = models.ForeignKey("Material", on_delete=models.SET_NULL, verbose_name="材质")  # 材质


class Material(BaseModel):
    """材质"""
    number = models.CharField(max_length=8, verbose_name="材质编号")
    material = models.CharField(max_length=16, verbose_name="材质")

    class Meta:
        ordering = ["id"]
        db_table = "tb_material"
        verbose_name = "材质"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.material
