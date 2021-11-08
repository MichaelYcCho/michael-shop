from rest_framework import pagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializer


@permission_classes([AllowAny])
@api_view(['GET'])
def product_list(request):
    category = request.GET.get('category')


    if category == 'main':
        products = Product.objects.all().order_by('-created_at')[:4]
    else:
        products = Product.objects.all().order_by('-created_at')

    paginator = PageNumberPagination()
    paginator.page_size = 6

    results = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)