from django.db import models
from utils._base_model import base_model


from alloy.models import Alloy


class Client(base_model.BaseModel):
    """客户"""
    number = models.CharField(max_length=8, verbose_name="客户编号", help_text="客户编号")
    name = models.CharField(max_length=32, verbose_name="客户名称", help_text="客户名称")
    abbr = models.CharField(default=" ", max_length=64, verbose_name="客户简介", help_text="客户简介")
    address = models.CharField(default=" ", max_length=256, verbose_name="客户地址", help_text="客户地址")
    belong = models.ForeignKey("ClientBelong", on_delete=models.SET_NULL, null=True, blank=True)
    industry = models.ForeignKey("ClientIndustry", on_delete=models.SET_NULL, null=True, blank=True, verbose_name
    ="客户性质")
    product_type = models.ForeignKey("ClientProductType", on_delete=models.SET_NULL, null=True, blank=True, verbose_name
    ="产品行业")
    mark = models.ForeignKey("ClientMark", on_delete=models.SET_NULL, null=True, blank=True, verbose_name
    ="客户等级")
    type = models.ForeignKey("ClientType", on_delete=models.SET_NULL, null=True, blank=True, verbose_name
    ="客户类型")

    class Meta:
        ordering = ["name", "-id"]
        db_table = "tb_client"
        verbose_name = "客户"
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        展示客户名称
        :return:
        """
        return "客户名称:{}".format(self.name)


class ClientAlloy(base_model.BaseModel):
    """客户产品相关"""
    alloy = models.ForeignKey(Alloy,on_delete=models.SET_NULL,null=True,blank=True)  # 关联合金


    class Meta:
        db_table = "tb_client_alloy"
        verbose_name ="客户产品合金"




# class ClientProblem(base_model.BaseModel):
#     """"客户产品问题"""


class ClientComplaint(base_model.BaseModel):
    """客户投诉"""
    complaint = models.CharField(max_length=256,verbose_name="客户投诉")
    image = models.URLField(default="",verbose_name="客户投诉图片")
    analyse = models.ForeignKey("ClientComplaintAnalyse",on_delete = models.SET_NULL,null=True,blank = True,
                                verbose_name="客户投诉分析")
    client = models.ForeignKey("Client",on_delete = models.SET_NULL,null=True,blank= True,verbose_name="客户")

class ClientDifficult(base_model.BaseModel):
    """客户难点异常"""
    difficult = models.TextField(verbose_name="客户难点记录")
    client = models.ForeignKey("Client",on_delete=models.SET_NULL,null=True,blank=True,verbose_name="客户")

    class Meta:
        db_table= "tb_client_difficult"
        verbose_name= "客户难点"
        verbose_name_plural = verbose_name

class ClientComplaintAnalyse(base_model.BaseModel):
    """客户投诉分析"""
    analyse = models.TextField(verbose_name="客户投诉分析")
    class Meta:
        db_table = "tb_client_complaint_analyse"
        verbose_name="客户投诉分析"
        verbose_name_plural = verbose_name


class ClientMark(base_model.BaseModel):
    """客户等级"""
    mark = models.CharField(max_length=32, verbose_name="客户等级")

    class Meta:
        db_table = "tb_client_mark"
        verbose_name = "客户"
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        展示客户等级
        :return:
        """
        return "客户等级:{}".format(self.mark)


class ClientType(base_model.BaseModel):
    """客户类型"""
    type = models.CharField(max_length=32, verbose_name="客户类型")

    class Meta:
        db_table = "tb_client_type"
        verbose_name = "客户类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        展示客户名类型
        :return:
        """
        return "客户类型:{}".format(self.type)


class ClientIndustry(base_model.BaseModel):
    """
    客户所属性质
    """
    industry = models.CharField(max_length=32, verbose_name="所属行业")

    class Meta:
        db_table = "tb_client_industry"
        verbose_name = "所属行业"
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        展示客户名类型
        :return:
        """
        return "所属行业:{}".format(self.industry)


class ClientProductType(base_model.BaseModel):
    """
    客户产品所属行业类型
    """
    type = models.CharField(max_length=32, verbose_name="产品所属类型")

    class Meta:
        db_table = "tb_client_product_type"
        verbose_name = "产品所属类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        展示产品所属类型
        :return:
        """
        return "产品所属类型:{}".format(self.type)


class ClientBelong(base_model.BaseModel):
    """
    客户所属销售人员
    """
    belong = models.CharField(max_length=32, verbose_name="客户所属")

    class Meta:
        db_table = "tb_client_belong"
        verbose_name = "客户所属"
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        展示客户所属
        :return:
        """
        return "客户所属:{}".format(self.belong)
