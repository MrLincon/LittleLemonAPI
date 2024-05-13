import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3
    DELIVERY_CREW = 4
    CUSTOMER = 5

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee'),
        (DELIVERY_CREW, 'DeliveryCrew'),
        (CUSTOMER, 'Customer'),
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=5)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
