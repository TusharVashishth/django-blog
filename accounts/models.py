from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core import validators


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(validators=[validators.MinLengthValidator(10) ,validators.MaxLengthValidator(10)] ,max_length=20)
    image = models.ImageField(upload_to='userProfile/', null=True)
    facebook_url = models.URLField(max_length=200, null=True)
    instagram_url = models.URLField(max_length=200, null=True)
    twitter_url = models.URLField(max_length=200, null=True)
    about = models.TextField(validators=[validators.MinLengthValidator(50)] , max_length=1000 , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
