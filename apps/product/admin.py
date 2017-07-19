from django.contrib import admin
from .models import Product, Category


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'cost_price', 'price', 'count']
    fields = ('category', 'name', 'image', 'barcode', 'cost_price', 'price', 'count')
    model_icon = "fa fa-product-hunt"


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    fields = ('name', 'sort')
    model_icon = "fa fa-bars"


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
