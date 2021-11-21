from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.views.register_view import register
from accounts.views.login_view import LogIn, TokenTestView, kakao_callback
from accounts.views.profile_view import getuserProfile




urlpatterns = [
    path('register', register, name='register'),
    path('login', LogIn.as_view(), name='login'),
    path("login/kakao/callback", kakao_callback, name="kakao_callback"),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile', getuserProfile, name="user-profile"),
    path('hello', TokenTestView.as_view(), name="hello"),

]