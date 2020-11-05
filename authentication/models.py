from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('e-mail address'), unique=True)
    first_name = models.CharField(max_length=50, verbose_name=_('first name'), blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name=_('last name'), blank=True, null=True)
    company_name = models.CharField(max_length=100, verbose_name=_('company name'), blank=True, null=True)
    telegram = models.CharField(max_length=50, verbose_name=_('telegram'), blank=True, null=True)
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
