from django.db import models

# Create your models here.


class Merchant(models.Model):
    name = models.CharField('商户名', max_length=70)
    address = models.CharField('商户地址', max_length=300)
    boss_name = models.CharField('老板姓名', max_length=20)
    phone_number = models.CharField('联系电话', max_length=20)
    bank_number = models.CharField('银行卡号', max_length=30)
    commission_rate = models.FloatField('佣金比例', blank=True)
    business_license = models.ImageField('营业执照', upload_to='business_license', blank=True)
    ID_number = models.CharField('身份证号码', max_length=30, blank=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name
