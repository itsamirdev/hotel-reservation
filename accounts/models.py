from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


class CustomUserManager(UserManager):
    def _create_user(self, phone, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone:
            raise ValueError("The given phone must be set")
        user = self.model(phone=phone, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, email, password, **extra_fields)


class User(AbstractUser):
    class Gender(models.TextChoices):
        NONE = "NONE"
        MALE = "MALE"
        FEMALE = "FEMALE"

    username = None
    email = models.EmailField(blank=True, unique=True)
    phone = models.CharField(max_length=16, unique=True)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.NONE)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True)
    national_id = models.CharField(max_length=10, unique=True, blank=True)
    avatar = models.ImageField(upload_to='images/avatars/', blank=True, null=True)
    is_valid = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.phone
