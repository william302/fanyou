from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MerchantUser

# Register your models here.
# class MerchantUserAdmin(UserAdmin):
#     add_form = MerchantUserCreationForm
#     form = MerchantUserChangeForm
#     model = MerchantUser
#     list_display = ['email', 'username',]

admin.site.register(MerchantUser, UserAdmin)