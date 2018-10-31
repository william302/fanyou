from django.test import TestCase
from django.urls import reverse
from accounts.models import MerchantUser


class LoginRequiredPasswordChangeTests(TestCase):
    def test_redirection(self):
        url = reverse('accounts:password_change')
        login_url = reverse('accounts:login')
        response = self.client.get(url)
        print(response.url)
        self.assertRedirects(response, '/accounts/login/?next=/accounts/password_change/')


class PasswordChangeTests(TestCase):
    def setUp(self, data={}):
        self.url = reverse('accounts:password_change')
        self.user = MerchantUser.objects.create_user(username='john', email='john@testss.com', password='old_password')
        self.client.login(username='john', password='old_password')
        self.response = self.client.post(self.url, data, follow=True)

    def test_login(self):
        url = reverse('index')
        response = self.client.get(url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class SuccessfulPasswordChangeTests(PasswordChangeTests):
    def setUp(self):
        super().setUp(data={'old_password': 'old_password',
                            'new_password1': 'new_password',
                            'new_password2': 'new_password'})

    # def test_redirection(self):
    #     self.assertRedirects(self.response, reverse('accounts:password_change_done'))

    def test_password_changged(self):
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('new_password'))

    def test_user_authentication(self):
        url = reverse('index')
        response = self.client.get(url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)