from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
            self, email, first_name, last_name, phone, password=None
    ):
        if not email:
            raise ValueError("must have user email")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.is_superuser = False
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name= 'super',
            last_name= 'admin',
            phone= '0'
        )
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class LoginType(models.TextChoices):
        LOGIN_EMAIL = "Email",
        LOGIN_KAKAO =  "Kakao"


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    login_type = models.CharField(
        max_length=50,
        choices=LoginType.choices,
        default=LoginType.LOGIN_EMAIL
    )
    email = models.EmailField(max_length=200, unique=True)
    email_checked = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    special_code = models.CharField(max_length=10, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


    USERNAME_FIELD = "email"


    def __str__(self):
        return str(f'{self.first_name} {self.last_name}')

