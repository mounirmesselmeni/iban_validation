from django.views.generic import FormView
from django.contrib import messages

from .forms import IbanSwiftForm


class IbanSwiftView(FormView):

    form_class = IbanSwiftForm
    template_name = "iban_form.html"
    success_url = "/"

    def form_valid(self, form):
        messages.success(self.request,
                         'Your information has been successfully submitted.')
        return super(IbanSwiftView, self).form_valid(form)
