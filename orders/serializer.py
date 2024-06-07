from rest_framework import serializers

from menu.models import Category, Item
from .models import Cart

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

# class CartItemSerializer(serializers.ModelSerializer):
#     item_id = serializers.UUIDField(source='item_id._id')
#     item_name = serializers.CharField(source='item_id.name')
#     category_name = serializers.CharField(source='item_id.category_id.name')
#     price = serializers.DecimalField(source='item_id.price', max_digits=6, decimal_places=2)
#
#     class Meta:
#         model = Cart
#         fields = ['item_id', 'item_name', 'category_name', 'price', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    user_id = serializers.UUIDField(source='user._id')

    class Meta:
        model = Cart
        fields = ['_id', 'user_id', 'items']

    def get_items(self, obj):
        cart_items = Cart.objects.filter(user=obj.user)
        return CartItemSerializer(cart_items, many=True).data
