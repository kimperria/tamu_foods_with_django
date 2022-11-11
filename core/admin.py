from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from tamueats.admin import FoodProductAdmin
from tamueats.models import FoodProduct
from tags.models import TaggedItem
from .models import User


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
                "fields": ("username", "password1", "password2", 'email', 'first_name', 'last_name'),
            },
        ),
    )


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