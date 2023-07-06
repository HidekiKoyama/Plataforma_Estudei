from django.urls import path
from .views import system_login

urlpatterns = [
    path('', system_login.index, name="index"),
]
