from rest_framework import serializers

from menu.models import Category, Item
from .models import Cart, OrderItem, Order


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['_id', 'item_id', 'quantity', 'customer_id']


class CartItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item_id.name', read_only=True)
    customer_email = serializers.EmailField(source='customer_id.email', read_only=True)
    category_name = serializers.CharField(source='item_id.category_id.name', read_only=True)
    price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['_id', 'category_name', 'item_name', 'quantity', 'price', 'customer_email']

    def get_price(self, obj):
        return obj.quantity * obj.item_id.price

class OrderItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item_id.name', read_only=True)
    category_name = serializers.CharField(source='item_id.category_id.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['_id', 'item_id', 'item_name', 'category_name', 'quantity', 'price']

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['_id', 'customer_id', 'total_price']

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    customer_email = serializers.EmailField(source='customer_id.email', read_only=True)

    class Meta:
        model = Order
        fields = ['_id', 'customer_id', 'customer_email', 'created_at', 'total_price', 'order_items']
