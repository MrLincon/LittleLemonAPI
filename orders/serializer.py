from django.db import models
from rest_framework import serializers

from menu.models import Item, Category
from .models import Orders


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = [
            'uid',
            'customer_uid',
            'item_uid',
            'price',
            'category_uid',
        ]

    def validate(self, data):
        item_uid = data.get('item_uid')
        category_uid = data.get('category_uid')

        # Debug logs
        print(f"Validating item_uid: {item_uid}")
        print(f"Validating category_uid: {category_uid}")

        if not Item.objects.filter(uid=item_uid).exists():
            print(f"Item with uid {item_uid} does not exist")
            raise serializers.ValidationError({"item_uid": "Item does not exist!"})

        if not Category.objects.filter(uid=category_uid).exists():
            print(f"Category with uid {category_uid} does not exist")
            raise serializers.ValidationError({"category_uid": "Category does not exist!"})

        return data
