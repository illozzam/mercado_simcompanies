from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'thumbnail_logo', 'company_name', 'telegram')
    list_editable = ('is_staff', 'is_active', 'company_name', 'telegram')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Data and Company', {'fields': ('first_name', 'last_name', 'company_logo', 'company_name', 'telegram')}),
        ('Contract', {'fields': ('contract',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
