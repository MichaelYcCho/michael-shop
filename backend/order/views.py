from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from order.models import Order, OrderItem
from order.serializers import OrderSerializer


@api_view(['GET'])
def order_list_api(request):
    
    user = request.user
    
    if user.is_anonymous:
        data = {'message' : '로그인이 필요합니다'}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    else: 
        orders = Order.objects.filter(user=user)
        order_serializer = OrderSerializer(orders, many=True)
        return Response(order_serializer.data)


@api_view(['POST'])
def checkout_order_api(request):
    request_data = request.data
    user = request.user

    if user.is_anonymous:
        data = {'message' : '로그인이 필요합니다'}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    else: 
        order = Order(
                user = request.user,
                receiver_name = request_data['buyer_name'],
                receiver_email = request_data['buyer_email'],
                receiver_phone = request_data['buyer_tel'],
                apartment = request_data['apartment'],
                country = request_data['country'],
                city = request_data['city'],
                street_name = request_data['street_name'],
                post_code = request_data['post_code'],
                additional_message = request_data['additional_message'],
                total_price = request_data['amount'],
                )
        order.save()
        order_items = request_data['cartItems']
        
        for item in order_items:
            order_item = OrderItem(
                order = order,
                product_id = item['pk'],
                qty = item['quantity'],
                price = item['price'],
            )
            order_item.save()
            
        
        data = {'success': '성공', 'order_id': order.id}
        return Response(data, status=status.HTTP_200_OK)

 
@api_view(['POST'])
def checkout_complate_api(request):
    request_data = request.data
    user = request.user

    if user.is_anonymous:
        data = {'message' : '로그인이 필요합니다'}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    else: 
        order = Order.objects.get(pk=request_data['order_id'])
        order.imp_uid = request_data['merchant_uid']
        order.receipt_url = request_data['receipt_url']
        order.is_paid = True
        order.save()
        data = {'success': '성공'}
        return Response(data, status=status.HTTP_200_OK)



@api_view(['PUT'])
def delivery_confirm_api(request):
    user = request.user
    try:
        request_data = request.data
        order_id = request_data['order_id']
        order = Order.objects.get(pk=order_id)
        order.is_delivered = True
        order.save()
        orders = Order.objects.filter(user=user)
        order_serializer = OrderSerializer(orders, many=True)
        return Response(order_serializer.data)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    