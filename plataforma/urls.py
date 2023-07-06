from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('system/', include('sistema.urls')),
    path('', include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
