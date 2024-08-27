from django.urls import path

from .api_views import *

urlpatterns = [
    path('category1', Category1List.as_view()),
    path('category1/add', CreateCategory1.as_view()),
    path('category1/delete/<int:pk>', DeleteCategory1.as_view()),
    path('category1/update/<int:pk>', UpdateCategory1.as_view()),

    path('category2', Category2List.as_view()),
    path('category2/add', CreateCategory2.as_view()),
    path('category2/delete/<int:pk>', DeleteCategory2.as_view()),
    path('category2/update/<int:pk>', UpdateCategory2.as_view()),

    path('category3', Category3List.as_view()),
    path('category3/add', CreateCategory3.as_view()),
    path('category3/delete/<int:pk>', DeleteCategory3.as_view()),
    path('category3/update/<int:pk>', UpdateCategory3.as_view()),

    path('category4', Category4List.as_view()),
    path('category4/add', CreateCategory4.as_view()),
    path('category4/delete/<int:pk>', DeleteCategory4.as_view()),
    path('category4/update/<int:pk>', UpdateCategory4.as_view()),

]
