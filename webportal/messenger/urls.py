from django.urls import path
from .views import ViewReport

urlpatterns = [
    path('report/<int:pk>', ViewReport.as_view())
]
