from django.urls import path
from .api_views import RetrieveAuthenticatedUser
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user', RetrieveAuthenticatedUser.as_view()),
    path('login', obtain_auth_token)
]
