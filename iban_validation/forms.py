from django import forms
from django_iban.forms import IBANFormField, SWIFTBICFormField


class IbanSwiftForm(forms.Form):

    iban = IBANFormField()
    swift_bic = SWIFTBICFormField()
