from django.db import models
from userinfo.models import *
from sale.models import *

# Create your models here.
order_choice = (
    (0, "待支付"),
    (1, "已支付"),
    (2, "订单已取消"),
    (3, "订单失败"),
    (4, "订单成功"),
)

class Cartinfo(models.Model):
    price = models.DecimalField("价格", max_digits=8, decimal_places=2)
    buser = models.ForeignKey(Userinfo)
    car = models.ForeignKey(Carinfo)

    def __str__(self):
        return self.buser.username

    class Meta:
        db_table = "cartinfo"
        verbose_name = "出价表"
        verbose_name_plural = verbose_name

class Orderinfo(models.Model):
    buser = models.ForeignKey(Userinfo, related_name="buser")
    suser = models.ForeignKey(Userinfo, related_name="suser")
    car = models.TextField("汽车")
    price = models.DecimalField("价格", max_digits=8, decimal_places=2)
    orderno = models.CharField("订单号", max_length=50, null=False)
    status = models.IntegerField("订单状态", choices=order_choice, default=0)
    datetime = models.DateTimeField("时间", auto_now=True)
    isdelete = models.BooleanField("是否删除", default=False)

    def __str__(self):
        return self.orderno

    class Meta:
        db_table = "orderinfo"
        verbose_name = "订单表"
        verbose_name_plural = verbose_name