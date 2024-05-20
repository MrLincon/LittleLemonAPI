from rest_framework import serializers

from menu.models import Category, Item
from .models import Cart

class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['_id',  'item', 'quantity', 'customer']

class CartItemSerializer(serializers.ModelSerializer):
    item_id = serializers.UUIDField(source='item._id')
    item_name = serializers.CharField(source='item.name')
    category_name = serializers.CharField(source='item.category.name')
    price = serializers.DecimalField(source='item.price', max_digits=6, decimal_places=2)

    class Meta:
        model = Cart
        fields = ['item_id', 'item_name', 'category_name', 'price', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    user_id = serializers.UUIDField(source='user._id')

    class Meta:
        model = Cart
        fields = ['_id', 'user_id', 'items']

    def get_items(self, obj):
        cart_items = Cart.objects.filter(user=obj.user)
        return CartItemSerializer(cart_items, many=True).data
