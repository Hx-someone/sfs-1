from django.db import models
from utils._base_model.base_model import BaseModel
from client.models import Client

_inspector = [
    (0, "检测人1"),
    (1, "检测人2"),
    (3, "检测人3"),
    (4, "检测人3"),
]

_team = [
    (0, "Li"),
    (1, "Xiong")
]


class Salt(BaseModel):
    """盐"""

    number = models.CharField(max_length=8, verbose_name="盐编号", help_text="盐编号")


class SaltCheck(BaseModel):
    """
    炉盐检测
    """

    number = models.CharField(max_length=14, verbose_name="检测编号", help_text="检测编号")
    cn = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰根浓度", help_text="氰根浓度")  # 最多为5位，2位整数，3位小数
    co3 = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="碳酸根浓度", help_text="碳酸根浓度")
    cno = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰酸根浓度", help_text="氰酸根浓度")
    n_count = models.SmallIntegerField(verbose_name="生产炉数", help_text="生产炉数")
    b_total = models.DecimalField(max_digits=4,decimal_places=3, verbose_name="调整盐添加量", help_text="调整盐添加量")
    a_total = models.DecimalField(max_digits=4, decimal_places=3,verbose_name="基盐添加量", help_text="基盐添加量")
    image = models.URLField(default="", verbose_name="盐浴状态图", help_text="盐浴状态图")
    check_time = models.DateField(verbose_name="检测日期", help_text="检测日期")
    inspector = models.SmallIntegerField(default=0, choices=_inspector, verbose_name="检测人", help_text="检测人")

    class Meta:
        ordering = ["-number", "-id"]
        db_table = "tb_salt_check"
        verbose_name = "炉盐检测"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "炉盐检测:" + self.number

    # n_number = models.ForeignKey()


class SaltNew(BaseModel):
    """
    新盐检测
    """
    number = models.CharField(max_length=14, verbose_name="检测编号", help_text="检测编号")
    cn = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰根浓度", help_text="氰根浓度")  # 最多为5位，2位整数，3位小数
    co3 = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="碳酸根浓度", help_text="碳酸根浓度")
    cno = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰酸根浓度", help_text="氰酸根浓度")
    thaw_date = models.DateField(verbose_name="化盐日期", help_text="化盐日期")
    team = models.SmallIntegerField(default=0, choices=_team, verbose_name="化盐班组", help_text="化盐班组")
    check_time = models.DateField(verbose_name="检测日期", help_text="检测日期")
    inspector = models.SmallIntegerField(default=0, choices=_inspector, verbose_name="检测人", help_text="检测人")

    class Meta:
        ordering = ["-number", "-id"]
        db_table = "tb_salt_new"
        verbose_name = "新盐检测"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "新盐检测:" + self.number


class SaltClient(BaseModel):
    """
    客户来盐
    """
    number = models.CharField(max_length=14, verbose_name="检测编号", help_text="检测编号")
    cn = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰根浓度", help_text="氰根浓度")  # 最多为5位，2位整数，3位小数
    co3 = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="碳酸根浓度", help_text="碳酸根浓度")
    cno = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰酸根浓度", help_text="氰酸根浓度")
    in_date = models.DateField(verbose_name="来盐日期", help_text="来盐日期")
    check_time = models.DateField(verbose_name="检测日期", help_text="检测日期")
    inspector = models.SmallIntegerField(default=0, choices=_inspector, verbose_name="检测人", help_text="检测人")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="来盐客户")

    class Meta:
        ordering = ["-number", "-id"]
        db_table = "tb_salt_client"
        verbose_name = "客户来盐"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "《{}》来盐".format(self.client.name)


class SaltNA(BaseModel):
    """基盐种类及其工艺"""
    pass

class SaltRB(BaseModel):
    """调整盐种类及其工艺"""
    pass

class SaltToNew(BaseModel):
    """新盐试制工艺统计"""
    pass

