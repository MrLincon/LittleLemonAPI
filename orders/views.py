from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from menu.models import Category
from .models import Orders
from .serializer import OrderSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.permissions import IsCustomer

class AddOrderView(APIView):
    # permission_classes = [IsAuthenticated, IsCustomer]
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print("Incoming request data:", request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            orders = serializer.save()

            response = {
                'message': 'Category added successfully',
                'data': {
                    'uid': orders.uid,
                    'customer_id': orders.customer_uid,
                    'item_id': orders.item_uid,
                    'name': orders.name,
                    'price': orders.price,
                    'category_name': orders.category_name,
                }
            }

            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)