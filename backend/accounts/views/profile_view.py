from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.conf import settings

from accounts.models import User
from accounts.serializers import UserSerializer
import jwt

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getuserProfile(request):

    user = request.user
    serializer = UserSerializer(user)

    return Response(status=status.HTTP_200_OK, data=serializer.data )