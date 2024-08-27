from django.urls import path
from .views import StartPage, Category1Interface, Category2Interface, Category3Interface, Category4Interface

urlpatterns = [
    path('category1interface', Category1Interface.as_view()),
    path('category2interface', Category2Interface.as_view()),
    path('category3interface', Category3Interface.as_view()),
    path('category4interface', Category4Interface.as_view()),
    path('overview', StartPage.as_view()),
]
