from django.db import models


# Create your models here.
from userinfo.models import *

status_choice = (
    (0, "审核中"),
    (1, "已审核"),
    (2, "待审核"),
    (3, "未通过"),
)


class Brand(models.Model):
    titile = models.CharField("品牌", max_length=50)
    logo = models.ImageField("logo", upload_to="img/logo", default="")
    newprice = models.DecimalField("新车价格", max_digits=8, decimal_places=2)
    isdelete = models.BooleanField("是否删除", default=False)

    def __str__(self):
        return self.titile

    class Meta:
        db_table = "brand"
        verbose_name = "品牌"
        verbose_name_plural = verbose_name


class Carinfo(models.Model):
    brand = models.ForeignKey(Brand)
    regist_data = models.DateField("上牌日期")
    engineno = models.CharField("发动机号", max_length=50)
    mileage = models.IntegerField("公里数")
    record = models.CharField("维修记录", max_length=200)
    price = models.DecimalField("期望成交价格", max_digits=8, decimal_places=2)
    picture = models.ImageField("汽车图片", upload_to="img/car")
    formalities = models.BooleanField("手续是否齐全", default=False)
    debt = models.BooleanField("是否有负债", default=False)
    promise = models.TextField(verbose_name="卖家承诺", null=True)
    status = models.IntegerField("审核状态", choices=status_choice)
    user = models.ForeignKey(Userinfo)
    isdelete = models.BooleanField("是否删除", default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "carinfo"
        verbose_name = "汽车信息"
        verbose_name_plural = verbose_name