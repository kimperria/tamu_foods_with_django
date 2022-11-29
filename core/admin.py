from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from tamueats.admin import FoodProductAdmin
from tamueats.models import FoodProduct
from tags.models import TaggedItem
from .models import User, Vendor, Merchant


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    '''
        Admin class to handle users implementation
    '''
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'email', 'first_name', 'last_name', "profile_photo","password1", "password2"),
            },
        ),
    )

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_per_page = 10

@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_per_page = 10

class TagInline(GenericTabularInline):
    '''
        Generic class to relate tamueats and tags application
    '''
    autocomplete_fields = ['tag']
    model = TaggedItem
    extra = 1


class CustomFoodProductAdmin(FoodProductAdmin):
    inlines = [TagInline]

admin.site.unregister(FoodProduct)
admin.site.register(FoodProduct, CustomFoodProductAdmin)