from django.urls import path
from django.contrib.auth import views as auth_views  # Import default Django authentication views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Route for login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Route for logout
    path('register/', views.register, name='register'),
]