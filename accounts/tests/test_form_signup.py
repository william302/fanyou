from django.test import TestCase
from accounts.forms import MerchantUserCreationForm


class SignupFormTests(TestCase):
    def test_form_has_fields(self):
        form = MerchantUserCreationForm()
        expected = ['username', 'email', 'password1', 'password2']
        actual = list(form.fields)
        self.assertEqual(expected, actual)
