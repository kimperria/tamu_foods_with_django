from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='HomePage'),
    path('menu/', views.menu_page, name='MenuPage'),
    path('cart/', views.cart_page, name='cart'),
    path('checkout/', views.checkout_page, name='checkout'),
    path('update_item/', views.update_item, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),

    #coming soon page template
    path('coming-soon/', views.coming_soon, name='ComingSoonPage'),
]