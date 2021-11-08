from django.urls import path

from products.views import product_list, product_detail


urlpatterns = [
    path('list', product_list, name='product_list'),
    path('detail/<str:pk>/', product_detail, name="product_detail"),

]