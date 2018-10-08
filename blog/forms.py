import re

from django import forms;
from django.core.exceptions import ValidationError


def mobile_validate(value):
    phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
    res = re.search(phone_pat, value)
    if not res:
        raise ValidationError('手机号码格式错误', code='invalid')


class SignupForm(forms.Form):
    phone = forms.CharField(label='手机号', max_length=11, error_messages={'required': "手机号不能为空"})
    verification_code = forms.CharField(label='验证码', max_length=6, error_messages={'required': "验证码不能为空"})

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
        res = re.search(phone_pat, phone)
        if not res:
            raise ValidationError('请输入正确的手机号')
        return phone

    def clean_verification_code(self):
        verify_code = self.cleaned_data['verification_code']
        verify_code_pat = re.compile('^\d{6}$')
        res = re.search(verify_code_pat, verify_code)
        if not res:
            raise ValidationError('验证码错误')
        return verify_code
