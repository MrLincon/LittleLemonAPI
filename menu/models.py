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
    category_uid = models.UUIDField()
    category_name = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name