from django.test import TestCase

from .forms import IbanSwiftForm


class IbanSwiftValidationTestCase(TestCase):

    def test_wrong_iban(self):
        form_data = {'iban_or_swift': 'ddsssssfffff'}
        form = IbanSwiftForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_wrong_swift(self):
        form_data = {'iban_or_swift': '545454sdssd54451121'}
        form = IbanSwiftForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_valid_iban(self):
        form_data = {'iban_or_swift': 'BE62510007547061'}
        form = IbanSwiftForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_valid_swift(self):
        form_data = {'iban_or_swift': 'BOFAUS3N'}
        form = IbanSwiftForm(data=form_data)
        self.assertEqual(form.is_valid(), True)
