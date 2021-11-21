from django.db import models

from accounts.models import User
from products.models import Product



class ORDER_TYPES(models.TextChoices):
        CARD = "Card",
        V_BANK =  "V_Bank"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    imp_uid = models.CharField(max_length=120, null=True, blank=True)
    receipt_url = models.CharField(max_length=255, blank=True, null=True)
    order_type = models.CharField(
        max_length=50,
        choices=ORDER_TYPES.choices,
        default=ORDER_TYPES.CARD
    )
    receiver_name = models.CharField(max_length=100)
    receiver_email = models.CharField(max_length=100)
    receiver_phone = models.CharField(max_length=100)
    apartment = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street_name = models.CharField(max_length=255)
    post_code = models.CharField(max_length=30)
    additional_message = models.TextField(blank=True, null=True)
    shipping_price = models.FloatField(default=0)
    total_price = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user}의 구매내역 - {self.pk}'
    
    class Meta:
        ordering = ['-created_at']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.product.name)

