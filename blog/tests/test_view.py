from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import index
from blog.models import Merchant
from blog.forms import SignupForm


class IndexTests(TestCase):
    def test_index_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve('/')
        self.assertEqual(view.func, index)


class MerchantTests(TestCase):
    # def setUp(self):
    #     Merchant.objects.create(name='宁波飞马', address='宁波市飞马街', boss_name='李飞马', mobile='13786784733',
    #                             bank_number='62238837498764932')
    #     url = reverse('merchant_detail', kwargs={'merchant_id': 99})
    #     self.response = self.client.get(url)
    # def test_merchant_detail_view_success_status_code(self):
    #     url = reverse('merchant_detail', kwargs={'merchant_id': 1})
    #     res = self.client.get(url)
    #     self.assertEqual(res.status_code, 200)

    def test_merchant_detail_view_not_found_status_code(self):
        url = reverse('merchant_detail', kwargs={'merchant_id': 99})
        self.response = self.client.get(url)
        self.assertEqual(self.response.status_code, 404)


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