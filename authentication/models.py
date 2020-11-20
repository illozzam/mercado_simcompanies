from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.html import format_html
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('endereço de e-mail'), unique=True)
    first_name = models.CharField(max_length=50, verbose_name=_('nome'), blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name=_('sobrenome'), blank=True, null=True)
    company_name = models.CharField(max_length=100, verbose_name=_('nome da empresa'), blank=True, null=True)
    company_logo = models.URLField(max_length=255, verbose_name=_('logotipo da empresa'), blank=True, null=True, help_text=_('Endereço do logotipo no site do SimCompanies'))
    telegram = models.CharField(max_length=50, verbose_name=_('telegram'), blank=True, null=True, help_text=_('Em breve, você poderá receber suas notificações via telegram'))
    contract = models.TextField(_('contract'), null=True, blank=True)
    is_staff = models.BooleanField(default=False, verbose_name=_('is staff'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('date joined'))
    last_login = models.DateTimeField(auto_now=True, verbose_name=_('last login'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def thumbnail_logo(self):
        return format_html('<img src="{}" height="48">', self.company_logo)
    thumbnail_logo.allow_tags = True

def get_deleted_user(self):
    '''
    Esta função cria um usuário "User Deleted" caso não exista e retorna esse usuário, caso exista.
    '''
    email_deleted = 'blank@deleted.nul'
    if User.objects.filter.get(email=email_deleted).exists():
        return User.objects.get(email=email_deleted)
    else:
        user = User.objects.create(email=email_deleted, first_name='User', last_name='Deleted')
        return user
