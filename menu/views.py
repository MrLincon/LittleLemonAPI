from .serializer import CategorySerializer, ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.permissions import IsAdmin
from .models import Category, Item


class AddCategoryView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = CategorySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            category = serializer.save()

            response = {
                'message': 'Category added successfully',
                'data': {
                    'uid': category.uid,
                    'name': category.name,
                }
            }

            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCategoryView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, category_uid):
        try:

            try:
                data = Category.objects.get(uid=category_uid)
            except Exception as e:
                print(e)
                return Response({
                    'data': {},
                    'message': 'Category not found!'
                }, status=status.HTTP_404_NOT_FOUND)


            serializer = CategorySerializer(data, data=request.data, partial=True)


            if serializer.is_valid():
                category = serializer.save()
                response = {
                    'message': 'Category updated successfully!',
                    'data': {
                        'uid': category.uid,
                        'name': category.name,
                    }
                }
                return Response(response, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class FetchCategoriesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(data=categories, many=True)

            serializer.is_valid()

            response = {
                'message': 'Categories fetched successfully!',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class AddItemView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = ItemSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid()

        if valid:
            item = serializer.save()
            response = {
                'message': 'Item added successfully',
                'data': {
                    'name': item.name,
                    'uid': item.uid,
                }
            }

            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateItemView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, item_uid):
        try:

            try:
                data = Item.objects.get(uid=item_uid)
            except Exception as e:
                print(e)
                return Response({
                    'data': {},
                    'message': 'Item not found!'
                }, status=status.HTTP_404_NOT_FOUND)


            serializer = ItemSerializer(data, data=request.data, partial=True)


            if serializer.is_valid():
                item = serializer.save()
                response = {
                    'message': 'Item updated successfully!',
                    'data': {
                        'uid': item.uid,
                        'name': item.name,
                        'category_uid': item.category_uid,
                    }
                }
                return Response(response, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class FetchItemsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            items = Item.objects.all()
            serializer = CategorySerializer(data=items, many=True)

            serializer.is_valid()

            response = {
                'message': 'Items fetched successfully!',
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class FetchItemsByCategoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, category_uid):
        try:
            items = Item.objects.filter(category_uid=category_uid)
            serializer = CategorySerializer(data=items, many=True)

            serializer.is_valid()

            response = {
                'message': 'Items fetched successfully!',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)