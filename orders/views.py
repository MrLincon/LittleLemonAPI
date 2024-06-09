from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import User, Item, Cart, Order, OrderItem
from .serializer import CartItemSerializer, CartCreateSerializer, OrderDetailSerializer, OrderCreateSerializer, OrderItemSerializer


class AddCartView(APIView):
    def post(self, request):
        item_id = request.data.get('item_id')
        quantity = request.data.get('quantity')
        customer_id = request.data.get('customer_id')

        try:
            item = Item.objects.get(_id=item_id)
            customer = User.objects.get(_id=customer_id)  # Ensure correct ID field
        except Item.DoesNotExist:
            return Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)


        cart_item_data = {
            'item_id': item._id,
            'quantity': quantity,
            'customer_id': customer._id
        }


        serializer = CartCreateSerializer(data=cart_item_data)
        if serializer.is_valid():
            cart_item = serializer.save()
            output_serializer = CartItemSerializer(cart_item)

            response = {
                'message': 'Items added to cart successfully!',
                'data': output_serializer.data,
            }

            return Response(response, status=status.HTTP_201_CREATED)

        print(f"serializer.errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchCartItemView(APIView):
    def get(self, request, customer_id):

        if customer_id:
            try:
                user = User.objects.get(_id=customer_id)
            except User.DoesNotExist:
                response = {
                    'message': 'Items added to cart successfully!',
                    'error': 'User not found!',
                }
                return Response(response, status=status.HTTP_404_NOT_FOUND)

            carts = Cart.objects.filter(customer_id=customer_id)
            serializer = CartItemSerializer(carts, many=True)
            response = {
                'message': 'Cart items fetched successfully!',
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)


class ConfirmOrderView(APIView):
    def post(self, request, customer_id):

        if not customer_id:
            return Response({"error": "customer_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            customer = User.objects.get(_id=customer_id)
        except User.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

        cart_items = Cart.objects.filter(customer_id=customer_id)
        if not cart_items:
            return Response({"error": "No items in the cart to confirm as order."}, status=status.HTTP_400_BAD_REQUEST)

        total_price = sum(item.quantity * item.item_id.price for item in cart_items)

        order_data = {
            'customer_id': customer._id,
            'total_price': total_price
        }
        order_serializer = OrderCreateSerializer(data=order_data)
        if order_serializer.is_valid():
            order = order_serializer.save()

            for cart_item in cart_items:
                order_item_data = {
                    'order_id': order,
                    'item_id': cart_item.item_id,
                    'quantity': cart_item.quantity,
                    'price': cart_item.quantity * cart_item.item_id.price
                }
                OrderItem.objects.create(**order_item_data)
                cart_item.delete()

            order_detail_serializer = OrderDetailSerializer(order)
            response = {
                'message': 'Order confirmed successfully!',
                'data': order_detail_serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FetchOrderView(APIView):
    def get(self, request, order_id):
        if not order_id:
            return Response({"error": "order_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(_id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderDetailSerializer(order)
        response = {
                'message': 'Ordered items fetched successfully!',
                'data': serializer.data
            }


        return Response(response, status=status.HTTP_200_OK)