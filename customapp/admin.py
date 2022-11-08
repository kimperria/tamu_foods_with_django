from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from tamueats.admin import FoodProductAdmin
from tamueats.models import FoodProduct
from tags.models import TaggedItem


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