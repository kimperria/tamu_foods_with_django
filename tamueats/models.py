from django.contrib import admin
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

class Discounts(models.Model):
    '''
     Class that defines promotions and discount on items 
    '''
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class FoodProductCategory(models.Model):
    '''
        Class that defines with category a food product belongs to
    '''
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('FoodProduct', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['title']



class FoodProduct(models.Model):
    '''
        Class that defines Food Product instance
    '''
    food_name = models.CharField(max_length=255)
    food_description = models.TextField()
    food_unit_price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(1)])
    inventory = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    last_update = models.DateTimeField(auto_now=True)
    food_category = models.ForeignKey(FoodProductCategory, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Discounts, blank=True)

    def __str__(self):
        return self.food_name


class Customer(models.Model):
    '''
    Class that defines Client instance 
    '''
    phone_number = models.CharField(max_length=255, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name


    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        # Double underscore to reference user instance
        ordering = ['user__first_name', 'user__last_name']

class FoodOrder(models.Model):
    '''
    Class that defince Order instance
        
        Args: 
            Time of order, Payment, customer and optional delivery on pay submission
    '''
    DELIVERY_STATUS_PENDING = 'P'
    DELIVERY_STATUS_DELIVERED = 'D'
    DELIVERY_STATUS_CHOICES = [
        (DELIVERY_STATUS_PENDING, 'pending'),
        (DELIVERY_STATUS_DELIVERED, 'delivered')
    ]

    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [ 
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length = 1,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING,
    )
    delivery_status = models.CharField(
        max_length = 1,
        choices = DELIVERY_STATUS_CHOICES,
        default = DELIVERY_STATUS_PENDING,
        null=True
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    # product = models.ForeignKey(FoodProduct, on_delete=models.PROTECT)

    def __str__(self):
        return f' {self.customer} Order'

class FoodOrderItem(models.Model):
    '''
        Class that handles order processing'
    '''
    food_order = models.ForeignKey(FoodOrder, on_delete = models.PROTECT)
    food_product = models.ForeignKey(FoodProduct, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(1)]
    )
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    '''
     Class that handles cart operations
    '''
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    '''
     Class that handles items in our clients cart
    '''
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()