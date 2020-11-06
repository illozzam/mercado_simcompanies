from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm, UserChangeForm as DjangoUserChangeForm
from .models import User

class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm):
        model = User
        fields = ('email', 'company_name', 'company_logo', 'telegram')

class UserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'company_logo', 'company_name', 'telegram')
