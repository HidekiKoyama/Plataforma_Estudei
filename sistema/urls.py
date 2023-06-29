from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('cad_user/', cad_user, name='cad_user'),
    path('system_index/', login_is_valid, name='login_is_valid'),
    path('cad_categories_curse/', cad_categories_curse, name="cad_categories_curse"),
]