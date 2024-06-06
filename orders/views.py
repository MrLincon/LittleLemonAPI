from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import User, Item, Cart
from .serializer import CartItemSerializer, CartSerializer, CartCreateSerializer, CartCreateOutputSerializer


class AddCartView(APIView):
    def post(self, request):
        item_id = request.data.get('item_id')
        quantity = request.data.get('quantity')
        customer_id = request.data.get('customer_id')

        # # Debugging prints to ensure data is being received
        # print(f"item_id: {item_id}, quantity: {quantity}, customer_id: {customer_id}")
        #
        # if not item_id or not quantity or not customer_id:
        #     return Response({"error": "Item ID, quantity, and customer ID are required."}, status=status.HTTP_400_BAD_REQUEST)
        #
        # # Make sure the item and customer exist
        try:
            item = Item.objects.get(_id=item_id)
            customer = User.objects.get(_id=customer_id)  # Ensure correct ID field
        except Item.DoesNotExist:
            return Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

        # Prepare the data for the serializer
        cart_item_data = {
            'item_id': item._id,   # ensure field name matches serializer field
            'quantity': quantity,
            'customer_id': customer._id  # ensure field name matches serializer field and correct ID field
        }

        # Debugging print to check data before passing to serializer
        print(f"cart_item_data: {cart_item_data}")

        serializer = CartCreateSerializer(data=cart_item_data)
        if serializer.is_valid():
            cart_item = serializer.save()
            output_serializer = CartCreateOutputSerializer(cart_item)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Debugging print to check validation errors
            print(f"serializer.errors: {serializer.errors}")
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