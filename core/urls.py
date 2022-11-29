from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_customer_account, name='SignUp'),
    path('register/specialrole', views.register_non_customer_account, name='Register'),
    path('login/', views.login_account, name='SignIn'),
    path('account/profile/', views.customer_profile , name='customer-profile'),
    path('dashboard/', views.dashboard , name='dashboard')
]