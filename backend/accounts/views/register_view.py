from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from accounts.models import User
from accounts.serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data = request.data, context = {'request': request})
    data = {}

    if serializer.is_valid():
        user = serializer.save()
        # 이메일 인증전까지 임시
        user.is_active = True
        user.save()
        data['response'] = 'Successfully registered new user'
        status_code = status.HTTP_201_CREATED
    else:
        data = serializer.errors
        # FIXME - EmailField에 대해서 선제적으로 validation을 잡아주어서 error raise가 불가
        status_code = status.HTTP_202_ACCEPTED
    return Response(status=status_code, data=data)