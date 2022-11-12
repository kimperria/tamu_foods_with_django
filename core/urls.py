from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_account, name='SignUp'),
    path('login/', views.login_account, name='SignIn'),
]