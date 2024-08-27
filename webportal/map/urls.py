from django.urls import include, re_path
from .views import MapPageView


urlpatterns = [
    # The map view
    re_path('map/', MapPageView.as_view(), name='map'),
]
