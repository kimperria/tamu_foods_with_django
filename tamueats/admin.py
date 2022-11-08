from django.contrib import admin
from django.db.models.aggregates import Count
from . import models

@admin.register(models.FoodProduct)
class FoodProductAdmin(admin.ModelAdmin):
    '''
        Admin class for foodProduct class
    '''
    list_display = ['food_name', 'food_unit_price', 'inventory_status', 'food_category_title']
    list_editable = ['food_unit_price']
    list_per_page = 10
    list_select_related = ['food_category']

    def food_category_title(self, foodProduct):
        return foodProduct.food_category.title

    @admin.display(ordering='inventory')
    def inventory_status(self, foodProduct):
        if foodProduct.inventory < 10:
            return 'Low'
        return 'OK'


@admin.register(models.FoodProductCategory)
class FoodProductCategoryAdmin(admin.ModelAdmin):
    '''
        Admin class for category

        args:
            Compute the amount of food products in a particular category
            defines a function that takes in the category to create a new attribute
            annotate the value from the query set method to the attribute function
    '''
    list_display = ['title', 'category_count']

    @admin.display(ordering='product_category_count')
    def category_count(self, foodProductCategory):
        return foodProductCategory.product_category_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_category_count = Count('foodproduct')
        )




@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''
    Admin class for customer 
    '''
    list_display = ['first_name', 'last_name', 'username','email_address', 'phone_number', 'registration_date']
    list_per_page = 10
    ordering = ['first_name', 'last_name']




@admin.register(models.FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    '''
    Admin class for orders
        methods: display, editable
    '''
    list_display = ['id', 'placed_at', 'customer','payment_status', 'delivery_status']
    list_editable = ['payment_status', 'delivery_status']