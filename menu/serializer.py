from django.db import models
from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['uid', 'name']

    def validate(self, data):
        name = data.get('name')

        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("This category already exists.")
        return data


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['uid', 'name', 'price', 'category_uid', 'is_featured']

    def validate(self, data):
        name = data.get('name')
        price = data.get('price')
        category_uid = data.get('category_uid')

        if Item.objects.filter(name=name).exists():
            raise serializers.ValidationError("This item already exists!")
        elif price <= 0.00:
            raise serializers.ValidationError("Invalid price!")
        elif not Category.objects.filter(uid=category_uid).exists():
            raise serializers.ValidationError("This category does not exist!")
        return data


class ItemFeaturingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'is_featured']

    def validate(self, data):
        name = data.get('name')

        if Item.objects.filter(name=name).exists():
            raise serializers.ValidationError("This item already exists!")
        return data
