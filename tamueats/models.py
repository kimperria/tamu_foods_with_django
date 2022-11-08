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
    featured_product = models.ForeignKey('FoodProduct', on_delete=models.SET_NULL, null=True, related_name='+')

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
    food_unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    food_category = models.ForeignKey(FoodProductCategory, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Discounts)

    def __str__(self):
        return self.food_name


class Customer(models.Model):
    '''
    Class that defines Client instance 
    '''
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.EmailField(unique=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']

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
    product = models.ForeignKey(FoodProduct, on_delete=models.PROTECT)

class FoodOrderItem(models.Model):
    '''
        Class that handles order processing'
    '''
    food_order = models.ForeignKey(FoodOrder, on_delete = models.PROTECT)
    food_product = models.ForeignKey(FoodProduct, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
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