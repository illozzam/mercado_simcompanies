from django.db import models
from authentication.models import User
from market.models import Product
from main.models import Log

class Request(models.Model):
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

    types = [
        ['V', 'Vendendo'],
        ['C', 'Comprando'],
    ]

    user_origin = models.ForeignKey(User, related_name='user_origin', on_delete=models.CASCADE)
    user_destination = models.ForeignKey(User, related_name='user_destination', on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=types)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    quality = models.IntegerField(default=0, choices=quality_choices)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    daily_contract = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} {} ({} {} Q{}) {}'.format(
            self.user_origin,
            self.type,
            self.user_destination,
            self.quantity,
            self.product.name,
            self.quality,
            'D' if self.daily_contract else '',
        )

    def mark_done(self):
        self.done = True
        self.save()

    def include_product(self, product_market, user_destination, quantity):
        if quantity <= product_market.quantity:
            self.user_origin = product_market.owner
            self.user_destination = user_destination
            self.type = product_market.type
            self.product = product_market.product
            self.quantity = quantity if quantity else product_market.quantity
            self.quality = product_market.quality
            self.price = product_market.price
            self.daily_contract = product_market.daily_contract
            self.save()

            Log.objects.create(
                user=self.user_destination,
                description='Requisitou {} de {} {} Q{} @ {} - {}.'.format(
                    'compra' if product_market.type=='V' else 'venda',
                    self.quantity,
                    self.product.name,
                    self.quality,
                    self.price,
                    self.user_origin

                )
            )

            if product_market.quantity == quantity:
                product_market.delete()
            else:
                product_market.quantity -= quantity
                product_market.save()
            return self
        else:
            return None

    def product_thumbnail(self):
        return self.product.thumbnail()
