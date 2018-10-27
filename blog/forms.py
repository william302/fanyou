import re

from django import forms;
from django.core.exceptions import ValidationError


class SignupForm(forms.Form):
    phone = forms.CharField(label='手机号', max_length=11, error_messages={'required': "手机号不能为空"})
    verification_code = forms.CharField(label='验证码', max_length=6, error_messages={'required': "验证码不能为空"})

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SignupForm, self).__init__(*args, **kwargs)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # if phone != self.request.session.get('phone', None):
        #     raise ValidationError('请输入正确的手机号')
        # return phone
        phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
        res = re.search(phone_pat, phone)
        if not res:
            raise ValidationError('请输入正确的手机号')
        return phone

    def clean_verification_code(self):
        verify_code = self.cleaned_data['verification_code']
        if verify_code == self.request.session.get('verify_code', None) and self.request.session.get('phone', None) == self.request.POST.get('phone'):
            pass
        else:
            raise ValidationError('验证码错误')
        return verify_code
