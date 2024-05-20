from django.conf import settings
from django.db import models
import uuid
from django.utils import timezone

from account.models import User
from menu.models import Item

class Cart(models.Model):
    _id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Cart of {self.customer.email}"