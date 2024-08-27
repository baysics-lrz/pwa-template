from django.urls import path
from .api_views import Category1Lexicon, Category2Lexicon, Category3Lexicon, Category4Lexicon

urlpatterns = [
    path('category1', Category1Lexicon.as_view()),
    path('category2', Category2Lexicon.as_view()),
    path('category3', Category3Lexicon.as_view()),
    path('category4', Category4Lexicon.as_view()),
]