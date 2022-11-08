from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='HomePage'),
    path('menu/', views.menu_page, name='MenuPage'),

    #coming soon page template
    path('coming-soon/', views.coming_soon, name='ComingSoonPage'),
]