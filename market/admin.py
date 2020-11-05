from django.contrib import admin
from .models import Product, ProductMarket, Log

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'name']

@admin.register(ProductMarket)
class ProductMarketAdmin(admin.ModelAdmin):
    list_display = ['product', 'owner', 'type', 'quantity', 'quality', 'price']
    list_editable = ['type', 'quantity', 'quality', 'price']
    ordering = ['type']

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'user']
