from django.contrib import admin
from .models import Request

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['user_origin', 'user_destination', 'product_thumbnail', 'quantity', 'quality', 'price', 'daily_contract']
    list_editable = ['quantity', 'price']
