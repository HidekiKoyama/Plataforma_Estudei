from django.urls import path
from .views_global import *
from .views_admin import Admin_space
from .views_user import *
from .views_teacher import *

urlpatterns = [
    path('cad_user/', cad_user, name='cad_user'),
    path('system_index/', login_is_valid, name='login_is_valid'),
    path('cad_categories_curse/', Admin_space.cad_categories_curse, name='cad_categories_curse'),
    path('update_cad_categories_curse/<int:id>/', Admin_space.update_cad_categories_curse, name='update_cad_categories_curse'),
    path('delete_categories_curse/<int:id>/', Admin_space.delete_categories_curse, name="delete_categories_curse"),
    path('home_admin/', Admin_space.home_admin, name='home_admin'),
    path('add_friend/', add_friend, name='add_friend'),
    path('add_courses/', add_courses, name='add_courses'),
    path('list_courses/', list_courses, name='list_courses'),
    path('profile_user/', profile_user, name='profile_user'),
    path('control_user/', Admin_space.control_user, name='control_user'),
]