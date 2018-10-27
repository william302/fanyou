from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import signup
from accounts.forms import MerchantUserCreationForm
from accounts.models import MerchantUser


# Create your tests here.
class SignUpTest(TestCase):
    def setUp(self):
        url = reverse('accounts:signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_url_resolve_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contain_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, MerchantUserCreationForm)

    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)


class SuccessfulSignupTests(TestCase):
    def setUp(self):
        url = reverse('accounts:signup')
        data = {
            'username': 'john',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)

    def test_user_creation(self):
        self.assertTrue(MerchantUser.objects.exists())

    def test_user_authentication(self):
        url = reverse('index')
        response = self.client.get(url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignupTests(TestCase):
    def setUp(self):
        url = reverse('accounts:signup')
        data = {}
        self.response = self.client.post(url, data)

    def test_sign_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(MerchantUser.objects.exists())
