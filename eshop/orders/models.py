from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from decimal import Decimal
from coupons.models import Coupon
from shop.models import Product
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    email = models.EmailField(_('email'),)
    address = models.CharField(_('address'), max_length=50)
    city = models.CharField(_('city'), max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon,
                               related_name='orders', null=True,
                               blank=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])

    def order_id(self):
        return self.id

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * \
               (self.discount /Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
