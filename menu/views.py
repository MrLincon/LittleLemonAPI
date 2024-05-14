from .serializer import CategorySerializer, ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.permissions import IsAdmin


class AddCategoryView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()

            response = {
                'message': 'Category added successfully',
                'data': {}
            }

            return Response(response, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
