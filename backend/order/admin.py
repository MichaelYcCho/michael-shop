from django.contrib import admin

from order.models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order_type', 'is_paid']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
