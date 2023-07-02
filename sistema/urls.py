from django.urls import path
from .views_global import *
from .views_admin import *
from .views_user import *
from .views_teacher import *

urlpatterns = [
    path('', index, name='index'),
    path('cad_user/', cad_user, name='cad_user'),
    path('system_index/', login_is_valid, name='login_is_valid'),
    path('cad_categories_curse/', cad_categories_curse, name='cad_categories_curse'),
    path('update_cad_categories_curse/<int:id>/', update_cad_categories_curse, name='update_cad_categories_curse'),
    path('delete_categories_curse/<int:id>/', delete_categories_curse, name="delete_categories_curse"),
    path('home_admin/', home_admin, name='home_admin'),
    path('add_friend/', add_friend, name='add_friend'),
    path('add_courses/', add_courses, name='add_courses'),
    path('list_courses/', list_courses, name='list_courses'),
]