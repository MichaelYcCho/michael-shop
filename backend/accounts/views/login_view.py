import os, requests, jwt
from django.http.response import JsonResponse

from django.conf import settings
from django.core.files.base import ContentFile
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from decouple import config

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

from accounts.models import User, LoginType
from accounts.serializers import LoginTokenSerializer



class LogIn(TokenObtainPairView):
    serializer_class = LoginTokenSerializer


class TokenTestView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class KakaoException(Exception):
    pass


def kakao_callback(request):
    try:
        code = request.GET.get("code")
        
        if settings.DEBUG == False:
            client_id = settings.DJANGO_KAKAO_ID
            redirect_uri = "http://158.247.224.15/accounts/login/kakao/callback"
        else:
            client_id = config("DJANGO_KAKAO_ID")
            redirect_uri = "http://localhost:3000/accounts/login/kakao/callback"
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
        )

        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException("Can't get authorization code.")
        kakao_access_token = token_json.get("access_token")
        kakao_refresh_token = token_json.get("refresh_token")
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {kakao_access_token}"},
        )
        profile_json = profile_request.json()
        kakao_account = profile_json.get("kakao_account")
        email = kakao_account.get("email", None)
        if email is None:
            raise KakaoException("Please also give me your email")
        profile = kakao_account.get("profile")
        nickname = profile.get("nickname")
        profile_image = profile.get("profile_image_url")

        # 유저는 존재하지만 카카오톡을 통해 로그인하지 않는 경우
        try:
            user = User.objects.get(email=email)
            if user.login_type != LoginType.LOGIN_KAKAO:
                raise KakaoException(f"Please log in with: {user.login_type}")
        except User.DoesNotExist:
            user = User.objects.create(
                email=email,
                first_name=nickname,
                last_name=nickname,
                login_type=LoginType.LOGIN_KAKAO,
                is_active=True,
            )
            user.set_unusable_password()
            user.save()
            # 프로필 사진이 있는지 확인
            if profile_image is not None:
                photo_request = requests.get(profile_image)
                # ContentFile()로 인하여 파일에 담기고  이 파일은 avater에 저장됨
                user.avatar.save(
                    f"{nickname}-avatar.png", ContentFile(photo_request.content)
                )
        access_token = jwt.encode({"id" : user.id}, settings.SECRET_KEY, algorithm="HS256")
        #decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms="HS256")
        context = {
            'status': 200,
            'data': 'success',
            'access_token': access_token,
        }

        return JsonResponse(context)
    except KakaoException as e:
        context = {
            "error": e.args[0],
            'data': 'fail'
        }
        return JsonResponse(context)