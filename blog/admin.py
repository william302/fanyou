from django.contrib import admin
from .models import Merchant
from .aliyun_oss import qrcode_upload
# Register your models here.


# class MerchantAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         obj.qrcode = qrcode_upload(obj.id)
#         super().save_model(request, obj, form, change)


admin.site.register(Merchant)
