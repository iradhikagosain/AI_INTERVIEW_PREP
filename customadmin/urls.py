from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
   path('admin/', admin.site.urls),
   path('users/', include('users.urls')),
   path('admin-login/', views.admin_login, name='admin_login'),
   path('admin-logout/', LogoutView.as_view(next_page='admin_login'), name='admin_logout'),
   path('admin-users/', views.user_list, name='admin_user_list'),
   path('dashboard/', views.dashboard, name='admin_dashboard'),
  
 ]
