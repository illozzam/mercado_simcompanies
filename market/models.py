from django.db import models
from django.utils.html import format_html
from authentication.models import User

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

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='produto')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=type_choices, null=True, blank=True, verbose_name='Deseja comprar ou vender?')
    quantity = models.IntegerField(verbose_name='quantidade')
    quality = models.IntegerField(default=0, choices=quality_choices, verbose_name='qualidade')
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='preço')
    description = models.TextField(verbose_name='Observações', null=True, blank=True)
    daily_contract = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.product.name, self.owner.company_name)
