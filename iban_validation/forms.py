from django import forms
from django.core.exceptions import ValidationError

from django_iban.validators import IBANValidator, swift_bic_validator


class IbanOrSwiftField(forms.CharField):

    def __init__(self, use_nordea_extensions=False, include_countries=None, *args, **kwargs):
        self.default_validators = [
            IBANValidator(use_nordea_extensions, include_countries),
            swift_bic_validator]
        super(IbanOrSwiftField, self).__init__(*args, **kwargs)

    def run_validators(self, value):
        if value in self.empty_values:
            return
        errors = []
        iban_valid = False
        swift_valid = False
        err_msg = "Invalid data, only IBAN or SWIFT are acceptable"
        for v in self.validators:
            try:
                v(value)
                if isinstance(v, IBANValidator):
                    iban_valid = True
                elif hasattr(v, '__name__') and v.__name__ == 'swift_bic_validator':
                    swift_valid = True
            except ValidationError as e:
                if hasattr(e, 'code') and e.code in self.error_messages:
                    e.message = self.error_messages[e.code]
                if isinstance(v, IBANValidator) or hasattr(v, '__name__') and v.__name__ == 'swift_bic_validator':
                    if err_msg not in errors:
                        errors.append(err_msg)
                else:
                    errors.extend(e.error_list)
        if errors and (not swift_valid and not iban_valid):
            raise ValidationError(errors)


class IbanSwiftForm(forms.Form):

    iban_or_swift = IbanOrSwiftField()
