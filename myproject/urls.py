from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

handler404 = 'myproject.views.custom_404_view'

urlpatterns = [
    path('custom-admin/', include('customadmin.urls')),
    path('users/', include('users.urls')),  
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
