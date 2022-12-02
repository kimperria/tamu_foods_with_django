from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from .models import FoodProduct, Customer, FoodOrder, FoodOrderItem

def index(request):
    '''
    Function view to display home page
    '''

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = FoodOrder.objects.get_or_create(customer=customer, payment_status='P')
        items = order.foodorderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items":0}
        cartItems = order['get_cart_items']
    
        
    context = {
        'cartItems':cartItems
    }
    return render(request, 'tamueats/homepage.html', context)

def menu_page(request):
    '''
    View function for the menu page
    '''
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = FoodOrder.objects.get_or_create(customer=customer, payment_status='P')
        items = order.foodorderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items":0}
        cartItems = order['get_cart_items']
    
        


    food_querry_set = FoodProduct.objects.all()
    context = {
        'order': order,
        'menu': food_querry_set,
        'cartItems':cartItems
    }
    return render(request, "tamueats/menu.html", context)

def cart_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = FoodOrder.objects.get_or_create(customer=customer, payment_status='P')
        items = order.foodorderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items":0}
        cartItems = order['get_cart_items']
    
        
    context = {
        'items':items,
        'order': order,
        'cartItems':cartItems
    }
    return render(request, 'tamueats/cart.html', context)

def checkout_page(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = FoodOrder.objects.get_or_create(customer=customer, payment_status='P')
        items = order.foodorderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items":0}
        cartItems = order['get_cart_items']
    
        
    context = {
        'items':items,
        'order': order,
        'cartItems':cartItems
    }

    return render(request, 'tamueats/checkout.html', context)

def update_item(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['action']

    print('Action:', action, 'ItemId:', itemId)

    customer = request.user.customer
    product = FoodProduct.objects.get(id=itemId)
    order, created = FoodOrder.objects.get_or_create(customer=customer, payment_status='P')

    orderItem, created = FoodOrderItem.objects.get_or_create(food_order=order, food_product=product)


    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()
    
    return JsonResponse("Item was added", safe=False)

def coming_soon(request):
    '''
    View function to render coming soon page
    '''
    return render(request, 'tamueats/comingsoon.html')