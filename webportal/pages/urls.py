from django.urls import include, re_path
from .views import ImpressumPageView, DataPolicyPageView, FAQPageView, HomePageView, \
    TermsOfUsePageView, DownloadsPageView, error_500, error_404

urlpatterns = [
    re_path('impressum/', ImpressumPageView.as_view(), name='impressum'),
    re_path('data-policy/', DataPolicyPageView.as_view(), name='datapolicy'),
    re_path('faq/', FAQPageView.as_view(), name='FAQ'),
    re_path(r'^$', HomePageView.as_view(), name='home'),
    re_path('terms-of-use/', TermsOfUsePageView.as_view(), name='termsofuse'),
    re_path('downloads/', DownloadsPageView.as_view(), name='downloads'),
    re_path('500/', error_500, name='error_500'),
    re_path('404/', error_404, name='error_404'),
    ]
