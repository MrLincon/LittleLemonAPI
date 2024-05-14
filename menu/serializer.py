from django.db import models
from rest_framework import serializers
from .models import Category, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

    def validate(self, data):
        name = data.get('name')

        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("This category already exists.")
        return data

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'category_uid']

    def validate(self, data):
        name = data.get('name')

        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("This item already exists.")
        return data
