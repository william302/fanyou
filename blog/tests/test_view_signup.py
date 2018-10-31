from django.test import TestCase
from django.urls import reverse
from blog.forms import SignupForm


class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.url = url
        self.response = self.client.get(url)

    # def test_csrf(self):
    #     self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_invalid_post_data_empty_fields(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '手机号不能为空')
        self.assertContains(response, '验证码不能为空')

    def test_signup_invalid_post_data(self):
        data = {'phone': 10876356745}
        response = self.client.post(self.url, data)
        form = response.context.get('form')
        self.assertContains(response, '请输入正确的手机号')
        self.assertTrue(form.errors)

    def test_contain_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignupForm)