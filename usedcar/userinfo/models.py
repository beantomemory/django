from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

sex_choice = (
    (0, "男"),
    (1, "女"),
)
role_choice = (
    (0, "买家"),
    (1, "卖家"),
    (2, "平台"),
)
bank_choice = (
    (0, "中国工商银行"),
    (1, "中国建设银行"),
    (2, "中国农业银行"),
    (3, "招商银行"),
    (4, "北京银行"),
    (5, "我家银行"),

)

class Userinfo(AbstractUser):
    # username = models.CharField(verbose_name="用户名", max_length=30, null=False)
    # password = models.CharField(verbose_name="密码", max_length=200, null = False)
    realname = models.CharField(verbose_name="真实姓名", max_length=30, null=False)
    iden = models.CharField(verbose_name="身份证号", max_length=18, null=False)
    ads = models.CharField(verbose_name="地址", max_length=200, null=False)
    uphone = models.CharField(verbose_name="手机号", max_length=20, null=False)
    sex = models.IntegerField(verbose_name="性别", choices=sex_choice, default=0)
    role = models.IntegerField(verbose_name="角色", choices=role_choice, default=0)
    isactive = models.BooleanField(verbose_name="是否激活", default = False)
    isban = models.BooleanField(verbose_name="是否禁用", default = False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "userinfo"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

class Bank(models.Model):
    cardno = models.CharField("卡号", max_length=30, null=False)
    user = models.ForeignKey(Userinfo)
    cpwd = models.CharField("交易密码", max_length=200, null=False)
    bank = models.IntegerField("开户银行", choices=bank_choice, default=0)
    isdelete = models.BooleanField("是否删除", default=False)

    def __str__(self):
        return self.bank

    class Meta:
        db_table = "bank"
        verbose_name = "银行卡"
        verbose_name_plural = verbose_name
