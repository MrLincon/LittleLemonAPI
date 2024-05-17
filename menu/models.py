import uuid
from django.db import models
from django.utils import timezone


class Category(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256, unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Item(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    category_uid = models.UUIDField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name