from django.conf.urls import patterns, url

from .views import IbanSwiftView

urlpatterns = patterns(
    '',
    url(r'^$', IbanSwiftView.as_view(), name='home'),
)
