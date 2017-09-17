from _decimal import Decimal

from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '<{0}> {1}:  ${2}'.format(self.__class__.__name__,
                                        self.name, self.price)


class Invoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='invoices')
    products = models.ManyToManyField(Product, related_name='invoices')
    created = models.DateField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    @property
    def total(self):
        return sum(self.products.values_list('price', flat=True))

    def __str__(self):
        return '<{0}> {1}: {2}'.format(self.__class__.__name__,
                                       self.user.email, self.created)
