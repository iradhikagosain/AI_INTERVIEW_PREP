from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),  
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('upload-resume/', views.upload_resume, name='upload_resume'),
]
