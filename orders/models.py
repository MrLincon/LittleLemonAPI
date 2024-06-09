from django.conf import settings
from django.db import models
import uuid
from django.utils import timezone

from account.models import User
from menu.models import Item

class Cart(models.Model):
    _id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='customer_id')
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, db_column='item_id')
    quantity = models.IntegerField()

    def __str__(self):
        return f"Cart of {self.customer_id}"

class Order(models.Model):
    _id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='customer_id')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer_id}"

class OrderItem(models.Model):
    _id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id', related_name='order_items')
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, db_column='item_id')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.item_id.name} in order {self.order_id}"