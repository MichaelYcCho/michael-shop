from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import User

import redis

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
            "phone",
            "special_code",
            "email_checked",
        )
        extra_kwargs ={'password':{'write_only':True}}
        read_only_fields = ("id", "email_checked" )
    

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'A user with that email already exists'})
        return email

    def validate_phone(self, phone):
        if len(phone) > 13:
            raise serializers.ValidationError('-을 포함하여 13글자를 넘을 수 없습니다')
        return phone

    def validate_first_name(self, value):
        return value.upper()
    
    def validate_last_name(self, value):
        return value.upper()
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)

        if password == confirm_password:
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError({'password': 'Both Passwords Must Be Matched!'})


class LoginTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        #r = redis.StrictRedis(host="localhost", port=6379, charset="utf-8", decode_responses=True)
        #r.set(f'{user.id}-refresh', str(token))

        # Add custom claims
        token['email'] = user.email
        #print(r.get(f'{user.id}-refresh'))

        return token