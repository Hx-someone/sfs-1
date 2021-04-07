from django.db import models
from utils._base_model.base_model import BaseModel


# processes = [
#     (0, "抛光"),
#     (1, "超声"),
#     (2, "预热"),
#     (3, "氮化"),
#     (4, "氧化"),
#     (5, "乳化"),
#     (6, "封闭"),
#     (7, "包装"),
#     (8, "清洗")
# ]
# idle = [
#     (0, "闲置"),
#     (1, "正常生产"),
#     (2, "报废")
# ]


class Idle(BaseModel):
    """设备状态"""
    status = models.CharField(max_length=16, verbose_name="状态")

    class Meta:
        ordering = ["status", "-id"]
        db_table = "tb_equipment_status"
        verbose_name = "状态"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "状态:{}".format(self.status)


class Processes(BaseModel):
    """设备所属工序"""
    process = models.CharField(max_length=16, verbose_name="工序")

    class Meta:
        ordering = ["process", "-id"]
        db_table = "tb_equipment_process"
        verbose_name = "工序"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "工序:{}".format(self.process)


class ProcessesKind(BaseModel):
    """工序种类"""
    kind = models.CharField(max_length=16, verbose_name="工序种类")
    process = models.ForeignKey("Processes", on_delete=models.CASCADE)

    class Meta:
        ordering = ["kind", "-id"]
        db_table = "tb_equipment_process_kind"
        verbose_name = "工序种类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "工序种类:{}".format(self.kind)


class Equipment(BaseModel):
    """设备"""
    number = models.CharField(max_length=32, verbose_name="设备编号")
    name = models.CharField(max_length=32, verbose_name="设备名称")
    size = models.CharField(max_length=32, verbose_name="设备尺寸")
    power = models.CharField(max_length=16, verbose_name="功耗")
    materials = models.CharField(max_length=16, verbose_name="材料")
    process = models.ForeignKey("Processes", on_delete=models.CASCADE, verbose_name="设备所属工序")
    idle = models.ForeignKey("Idle", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="设备状态")

    class Meta:
        db_table = "tb_equipment"
        verbose_name = "设备"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "设备名字:{}-{}".format(self.name, self.number)
