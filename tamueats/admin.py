from django.contrib import admin
from . import models

@admin.register(models.FoodProduct)
class FoodProductAdmin(admin.ModelAdmin):
    '''
        Admin class for foodProduct class
    '''
    list_display = ['food_name', 'food_unit_price', 'inventory_status']
    list_editable = ['food_unit_price']
    list_per_page = 10

    @admin.display(ordering='inventory')
    def inventory_status(self, foodProduct):
        if foodProduct.inventory < 10:
            return 'Low'
        return 'OK'


@admin.register(models.FoodProductCategory)
class FoodProductCategoryAdmin(admin.ModelAdmin):
    '''
        Admin class for category
    '''




@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''
    Admin class for customer 
    '''
    list_display = ['first_name', 'last_name', 'username','email_address', 'phone_number', 'registration_date']
    list_per_page = 10
    ordering = ['first_name', 'last_name']