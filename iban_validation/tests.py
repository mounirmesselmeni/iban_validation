from django.test import TestCase

from .forms import IbanSwiftForm


class IbanSwiftValidationTestCase(TestCase):

    def test_wrong_data(self):
        form_data = {
            'iban': 'ddsssssfffff',
            'swift_bic': '545454sdssd54451121'
        }
        form = IbanSwiftForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_valid_data(self):
        form_data = {
            'iban': 'BE62510007547061',
            'swift_bic': 'BOFAUS3N'
        }
        form = IbanSwiftForm(data=form_data)
        self.assertEqual(form.is_valid(), True)
