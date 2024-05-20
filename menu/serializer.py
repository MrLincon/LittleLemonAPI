from django.db import models
from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['_id', 'name']

    def validate(self, data):
        name = data.get('name')

        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("This category already exists.")
        return data


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['_id', 'name', 'price', 'category_id', 'is_featured']

    def validate(self, data):
        name = data.get('name')
        price = data.get('price')
        category_id = data.get('category_id')

        print(name)
        print(price)
        print(category_id._id)

        if Item.objects.filter(name=name).exists():
            raise serializers.ValidationError("This item already exists!")
        elif price <= 0.00:
            raise serializers.ValidationError("Invalid price!")
        elif not Category.objects.filter(_id=category_id._id).exists():
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
