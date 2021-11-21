from django.urls import path

from order.views import order_list_api, checkout_order_api, checkout_complate_api, delivery_confirm_api


urlpatterns = [
    path('list', order_list_api, name='order_list_api'),
    path('checkout', checkout_order_api, name='checkout_order_api'),
    path('checkout/complate', checkout_complate_api, name='checkout_complate_api'),
    path('delivery/confirm', delivery_confirm_api, name='delivery_confirm_api'),
]