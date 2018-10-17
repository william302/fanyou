from django.db import models
from .aliyun_oss import qrcode_upload
# Create your models here.


class Merchant(models.Model):
    name = models.CharField('商户名', max_length=20)
    address = models.CharField('商户地址', max_length=200)
    boss_name = models.CharField('老板姓名', max_length=20)
    mobile = models.CharField('联系电话', max_length=20)
    bank_number = models.CharField('银行卡号', max_length=30)
    commission_rate = models.FloatField('佣金比例', blank=True, null=True)
    business_license = models.ImageField('营业执照', upload_to='business_license', default='', blank=True, null=True)
    id_card_no = models.CharField('身份证号码', max_length=30, default='', blank=True, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)
    qrcode = models.CharField('二维码', max_length=200, default='', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        self.qrcode = qrcode_upload(self.id)
        super().save()
