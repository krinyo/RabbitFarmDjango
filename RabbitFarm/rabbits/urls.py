# rabbits/urls.py
from django.urls import path
from .views import rabbit_list, rabbit_detail

urlpatterns = [
    path('rabbit_list', rabbit_list, name='rabbit_list'),
    path('rabbit_detail/<int:pk>/', rabbit_detail, name='rabbit_detail'),
]
