import uuid
from django.utils import timezone
from django.db import models

class Orders(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    customer_uid = models.UUIDField(editable=False, default=uuid.uuid4)
    item_uid = models.UUIDField(blank=False)
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    category_name = models.CharField(max_length=256)
    category_uid = models.UUIDField()
    assigned_crew_id = models.UUIDField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name