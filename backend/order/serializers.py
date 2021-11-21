from rest_framework import serializers

from accounts.serializers import UserSerializer
from order.models import Order, OrderItem
from products.serializers import ProductSerializer



class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = (
                'product',
                'qty',
            )
        


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    order_items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)
    
    
    class Meta:
        model = Order
        fields = (  'pk',
                    'user',
                    'order_items',
                    'imp_uid',
                    'receipt_url',
                    'order_type',
                    'receiver_name',
                    'receiver_email',
                    'receiver_phone',
                    'apartment',
                    'country',
                    'city',
                    'street_name',
                    'post_code',
                    'additional_message',
                    'shipping_price',
                    'total_price',
                    'is_paid',
                    'is_delivered',
                    'delivered_at',
                    'created_at'
                    )