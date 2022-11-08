from django.contrib import admin
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html,  urlencode
from django.urls import reverse
from . import models



class QuantityFilter(admin.SimpleListFilter):
    '''
    Class that handle filtering food items by quantity in store
    '''
    title = 'quantity'
    parameter_name = 'quantityInStore'

    def lookups(self, request, model_admin):
        '''
            Return a list of tuples containing logic to implement
        '''
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset: QuerySet):
        '''
            Returns filtering logic    
        '''
        if self.value() == '<10':
            return queryset.filter(inventory=10)
@admin.register(models.FoodProduct)
class FoodProductAdmin(admin.ModelAdmin):
    '''
        Admin class for foodProduct class
    '''
    list_display = ['food_name', 'food_unit_price', 'inventory_status', 'food_category_title']
    list_editable = ['food_unit_price']
    list_per_page = 10
    list_filter = ['food_category', QuantityFilter,'last_update']
    list_select_related = ['food_category']

    def food_category_title(self, foodProduct):
        return foodProduct.food_category.title

    @admin.display(ordering='inventory')
    def inventory_status(self, foodProduct):
        if foodProduct.inventory <= 10:
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
        '''
         Redirect user to food item page
         '''
         #reverse method syntax admin:appname_url_view
         ## Define the dynamic url then append food product id
         ### Import urlencode utility to access category id 
         ### return an object with key name as url to search and value as a string of querried instance id
         #### Key value is class attribute with double underscore
        url = (
            reverse('admin:tamueats_foodproduct_changelist') 
            + '?' 
            + urlencode({
                "food_category__id" : str(foodProductCategory.id)
            }))
        return format_html('<a href="{}">{}</a>', url, foodProductCategory.product_category_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_category_count = Count('foodproduct')
        )




@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''
    Admin class for customer 
        search fields allow case sensitive search of character
    '''
    list_display = ['first_name', 'last_name', 'username','email_address', 'phone_number', 'registration_date']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']




@admin.register(models.FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    '''
    Admin class for orders
        methods: display, editable
    '''
    list_display = ['id', 'placed_at', 'customer','payment_status', 'delivery_status']
    list_editable = ['payment_status', 'delivery_status']