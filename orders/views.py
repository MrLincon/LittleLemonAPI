from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import User, Item, Cart
from .serializer import CartItemSerializer, CartSerializer, CartCreateSerializer


class AddCartView(APIView):
    def post(self, request):
        item = request.data.get('item_id')
        quantity = request.data.get('quantity')
        customer = request.data.get('customer_id')

        print(item)
        # Make sure the item and customer exist
        try:
            item = Item.objects.get(_id=item)
            customer = User.objects.get(_id=customer)
        except Item.DoesNotExist:
            return Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

        print(item.name)

        cart_item_data = {
            'item': item._id,
            'quantity': quantity,
            'customer': customer._id
        }

        print(cart_item_data)

        serializer = CartCreateSerializer(data=cart_item_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchCartItemView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        if user_id:
            try:
                user = User.objects.get(_id=user_id)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            carts = Cart.objects.filter(user=user)
            serializer = CartSerializer(carts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)