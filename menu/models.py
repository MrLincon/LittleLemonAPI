import uuid
from django.db import models
from django.utils import timezone


class Category(models.Model):
    _id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self._id)


class Item(models.Model):
    _id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self._id)