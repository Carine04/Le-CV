from django.urls import path

from .views import my_cv

urlpatterns = [
    path('',my_cv),
]