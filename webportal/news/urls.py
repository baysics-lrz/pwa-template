from django.urls import include, re_path
from .views import ArticleView


urlpatterns = [
    re_path('overview', ArticleView.as_view(), name='news'),
]