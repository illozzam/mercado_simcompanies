from django.db import models
from django.utils.html import format_html
from authentication.models import User

############## Auxiliary funcs ##############

def get_deleted_user(self):
    email_deleted = 'blank@deleted.nul'
    if User.objects.filter(email=email_deleted).exists():
        return User.objects.get(email=email_deleted)
    else:
        user = User.objects.create(email=email_deleted, first_name='User', last_name='Deleted')
        return user

############## Models ##############

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.URLField(max_length=255)

    def __str__(self):
        return self.name

    def thumbnail(self):
        return format_html('<img src="{}" height="64">', self.image)
    thumbnail.allow_tags = True

class ProductMarket(models.Model):
    quality_choices = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
    )

    type_choices = (
        ('V', 'Vendendo'),
        ('C', 'Comprando'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=type_choices, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    quality = models.IntegerField(default=0, choices=quality_choices)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    daily_contract = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.product.name, self.owner.company_name)

class Log(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET(get_deleted_user))
    description = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.date_time.isoformat(), self.description)
