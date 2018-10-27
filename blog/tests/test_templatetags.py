from django.test import TestCase
from django import forms
from blog.templatetags.form_tags import field_type, input_class


class ExampleForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ('name', 'password')


class FieldTypeTest(TestCase):
    def test_field_widget_type(self):
        form = ExampleForm()
        self.assertEqual('TextInput', field_type(form['name']))
        self.assertEqual(field_type(form['password']), 'PasswordInput')


class InputClassTest(TestCase):
    def test_unbound_field_class(self):
        form = ExampleForm()
        self.assertEqual('form-control ', input_class(form['name']))
        self.assertEqual('form-control ', input_class(form['password']))

    def test_valid_bound_field_class(self):
        form = ExampleForm({'name': 'john', 'password': '123'})
        self.assertEqual('form-control is-valid', input_class(form['name']))
        self.assertEqual('form-control ', input_class(form['password']))

    def test_invalid_bound_field_class(self):
        form = ExampleForm({'name': '', 'password': ''})
        self.assertEqual('form-control is-invalid', input_class(form['name']))
        self.assertEqual('form-control is-invalid', input_class(form['password']))
