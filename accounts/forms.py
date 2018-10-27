from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MerchantUser


class MerchantUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MerchantUser
        fields = ("username", "email")


class MerchantUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MerchantUser
        fields = ('username', 'email')
