from django.contrib import admin
from .models import Product, ProductMarket

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'name']

@admin.register(ProductMarket)
class ProductMarketAdmin(admin.ModelAdmin):
    list_display = ['product', 'owner', 'type', 'quantity', 'quality', 'price']
    list_editable = ['type', 'quantity', 'quality', 'price']
    ordering = ['type']
