from django.urls import include, re_path
from .views import send_contact

app_name = 'contact'

urlpatterns = [
    re_path('send/', send_contact, name='send_contact'),
]
