from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['url', 'title']
    list_editable = ['title']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['url']
        else:
            return []
