from django.contrib.auth.models import update_last_login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserRegistrationSerializer, SuperUserRegistrationSerializer, UserLoginSerializer, \
    PasswordChangeSerializer, UpdateRoleSerializer
from .permissions import IsAdmin, IsManager


class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            response = {
                'message': 'User successfully registered!',
                'data': {
                    '_id': user._id,
                    'username': user.username,
                    'email': user.email,
                    'role': user.role,
                    'access': access_token
                },
            }

            return Response(response, status=status.HTTP_201_CREATED)


class SuperUserRegistration(APIView):
    serializer_class = SuperUserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            response = {
                'message': 'User successfully registered!',
                'data': {
                    '_id': user._id,
                    'username': user.username,
                    'email': user.email,
                    'role': user.role,
                    'access': access_token
                },
            }

            return Response(response, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            update_last_login(None, user)

            response = {
                'message': 'Login successful!',
                'data': {
                    '_id': user._id,
                    'username': user.username,
                    'email': user.email,
                    'role': user.role,
                    'access': access_token
                },
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = PasswordChangeSerializer(data=request.data, context={'request': request})

            if serializer.is_valid():
                serializer.save()

                response = {
                    "message": "Password changed successfully.",
                    'data': {},
                }

                return Response(response, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)

            response = {
                'message': 'Internal Server Error',
                'data': {},
            }

            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateRoleView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        serializer = UpdateRoleSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():

            _id = serializer.validated_data['_id']
            role = serializer.validated_data['role']

            if role == User.ADMIN:
                return Response({'message': 'Role cannot be set to admin!'}, status=status.HTTP_403_FORBIDDEN)


            try:
                user = User.objects.get(_id=_id)
                user.role = role
                user.save()
                response_data = {
                    'message': 'Role updated successfully',
                    'data': {
                        '_id': user._id,
                        'username': user.username,
                        'email': user.email,
                        'role': user.role,
                    },
                }

                return Response(response_data, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                response_data = {'message': 'User not found', 'data': {}}
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

