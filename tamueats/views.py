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
        print(customer)
        order, created = FoodOrder.objects.get_or_create(customer=customer, payment_status='P')
        # order = FoodOrder.objects.get(customer=customer)
        print(order)
        items = order.foodorderitem_set.all()
    else:
        items = []
    print(list(items))
    for item in items:
        print(item)

    context = {
        'items':items
    }
    return render(request, 'tamueats/cart.html', context)

def checkout_page(request):

    return render(request, 'tamueats/checkout.html')

def coming_soon(request):
    '''
    View function to render coming soon page
    '''
    return render(request, 'tamueats/comingsoon.html')