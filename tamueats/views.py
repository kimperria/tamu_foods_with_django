from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodProduct, Customer, FoodOrder

def index(request):
    '''
    Function view to display home page
    '''
    return render(request, 'tamueats/homepage.html')

def menu_page(request):
    '''
    View function for the menu page
    '''
    # customers = Customer.objects.all()
    food_querry_set = FoodProduct.objects.all()
    return render(request, "tamueats/menu.html", {"menu":food_querry_set})

def cart_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = FoodOrder.objects.get_or_create(customer=customer, payment_status='P')
        items = order.foodorderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items":0}
    
        
    context = {
        'items':items,
        'order': order
    }
    return render(request, 'tamueats/cart.html', context)

def checkout_page(request):

    return render(request, 'tamueats/checkout.html')

def coming_soon(request):
    '''
    View function to render coming soon page
    '''
    return render(request, 'tamueats/comingsoon.html')