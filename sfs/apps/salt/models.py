from django.db import models
from utils._base_model.base_model import BaseModel
# from client.models import Client

"""
   检测编号规则：20210220A01PSN --->20210220 - A- 01- P- S - S
   日期+炉号+检测第次数+取样上下午+生产S+备用字母1位(用于新盐检测上中下)
       1.日期使用数字拼接：例：20210220
       2.炉号:英文大写字母排序，去掉容易混淆的字母：O,I,Z
           1#:A
           2#:B
           3#:C
           ...
           小#:S
           大#:T
           "大化盐炉为5#氮化炉，小化盐炉为6#氮化炉"
       3.检测次数:使用数字表示：例：第1次：01，第2次：02...
       4.取样上下午:
           1.上午(a.m)为:A
           2.下午(p.m)为:P
       5.倒数第二位:表示是生产、新盐、外来盐样、其他
           1.生产Product:P
           2.新盐new:N
           3.外来outside:O
           4.特殊special:S
       6.最后一位：备用位，
           1.用于新盐上下，S--->上,X-->下
           2.用户外来客户检测编号:A:编号1#，B:编号2#...
           3.如果都不是则是N
   """

_inspector = [
    (0, "检测人1"),
    (1, "检测人2"),
    (3, "检测人3"),
    (4, "检测人3"),
]

_team = [
    (0, "L"),
    (1, "X")
]

class SaltCheck(BaseModel):
    """
    炉盐检测
    """
    SALT_STATUS = [
        (0, "好"),
        (1, "良好"),
        (2, "一般"),
        (3, "差"),
        (4, "非常差")
    ]
    STOVE_NUMBER = [
        (0, "1#"),
        (1, "2#"),
        (2, "3#"),
        (3, "4#"),
        (4, "5#"),
        (5, "6#"),
        (6, "7#"),
        (7, "小#"),
        (8, "大#"),
    ]

    number = models.CharField(max_length=14, verbose_name="检测编号", help_text="检测编号")
    stove_number = models.SmallIntegerField(default=0, choices=STOVE_NUMBER,verbose_name="炉号", help_text="炉号")

    salt_na = models.ForeignKey("SaltNA",on_delete=models.SET_NULL,null = True,blank = True) # 盐种类

    cn = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰根浓度", help_text="氰根浓度")  # 最多为5位，2位整数，3位小数
    co3 = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="碳酸根浓度", help_text="碳酸根浓度")
    cno = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰酸根浓度", help_text="氰酸根浓度")
    n_count = models.SmallIntegerField(verbose_name="生产炉数", help_text="生产炉数")
    b_total = models.DecimalField(max_digits=4, decimal_places=3, verbose_name="调整盐添加量", help_text="调整盐添加量")
    a_total = models.DecimalField(max_digits=4, decimal_places=3, verbose_name="基盐添加量", help_text="基盐添加量")
    status = models.SmallIntegerField(default=1, choices=SALT_STATUS, verbose_name="盐浴状态", help_text="盐浴状态")
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
    LOCATION = [
        (0,"炉-上"),
        (1,"炉-下"),
        (2,"盘-上"),
        (3,"盘-下")
    ]
    number = models.CharField(max_length=14, verbose_name="检测编号", help_text="检测编号")

    salt_na = models.ForeignKey("SaltNA", on_delete=models.SET_NULL, null=True, blank=True)  # 盐种类

    salt_location = models.SmallIntegerField(default=0, choices=LOCATION, verbose_name="取样位置")
    cn = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰根浓度", help_text="氰根浓度")  # 最多为5位，2位整数，3位小数
    co3 = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="碳酸根浓度", help_text="碳酸根浓度")
    cno = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰酸根浓度", help_text="氰酸根浓度")
    thaw_date = models.DateField(verbose_name="化盐日期", help_text="化盐日期")
    team = models.SmallIntegerField(default=0, choices=_team, verbose_name="化盐班组", help_text="化盐班组")
    check_time = models.DateField(verbose_name="检测日期", help_text="检测日期")
    inspector = models.SmallIntegerField(default=0, choices=_inspector, verbose_name="检测人", help_text="检测人")
    batch = models.CharField(max_length=10, verbose_name="批号", help_text="批号")
    stove_number = models.SmallIntegerField(default=5,verbose_name="炉号")

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
    TYPE = [
        (0,"买盐客户"),
        (1,"加工客户"),
        (2,"潜在客户"),
        (3,"同类竞争")
    ]
    number = models.CharField(max_length=14, verbose_name="检测编号", help_text="检测编号")
    client = models.CharField(max_length=32, verbose_name="来料客户")
    type = models.SmallIntegerField(default=0,choices =TYPE,verbose_name="来盐类型")
    cn = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰根浓度", help_text="氰根浓度")  # 最多为5位，2位整数，3位小数
    co3 = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="碳酸根浓度", help_text="碳酸根浓度")
    cno = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="氰酸根浓度", help_text="氰酸根浓度")
    in_date = models.DateField(verbose_name="来盐日期", help_text="来盐日期")
    check_time = models.DateField(verbose_name="检测日期", help_text="检测日期")
    inspector = models.SmallIntegerField(default=0, choices=_inspector, verbose_name="检测人", help_text="检测人")


    class Meta:
        ordering = ["-number", "-id"]
        db_table = "tb_salt_client"
        verbose_name = "客户来盐"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "《{}》来盐".format(self.client)


class SaltNA(BaseModel):
    """基盐种类及其工艺"""
    name = models.CharField(max_length=16, verbose_name="N-A名字")
    type = models.CharField(max_length=16, verbose_name="N-A种类")
    new_salt_thaw_craft = models.CharField(max_length=128, verbose_name="新盐化盐融化工艺")
    using_salt_thaw_craft = models.CharField(max_length=64, verbose_name="新盐实用融化工艺")
    apply_alloy = models.CharField(max_length=64,verbose_name="适用合金")  # 这里关联合金表中的合金信息
    trait = models.CharField(max_length=128, verbose_name="特点")
    remark = models.CharField(max_length=256, verbose_name="备注")

    class Meta:
        ordering = ["name", "-id"]
        db_table = "tb_salt_na"
        verbose_name = "N-A盐"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "基盐:{}".format(self.name)


class SaltRB(BaseModel):
    """调整盐种类及其工艺"""
    name = models.CharField(max_length=16, verbose_name="N-B名字")
    type = models.CharField(max_length=16, verbose_name="N-B种类")
    add_craft = models.CharField(max_length=128, verbose_name="添加工艺")
    trait = models.CharField(max_length=256, verbose_name="特点")
    remark = models.CharField(max_length=256, verbose_name="备注")
    class Meta:
        ordering = ["name", "-id"]
        db_table = "tb_salt_nb"
        verbose_name = "N-B盐"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "调整盐:{}".format(self.name)