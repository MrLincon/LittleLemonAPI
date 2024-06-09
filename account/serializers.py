from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class SuperUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        auth_user = User.objects.create_superuser(**validated_data)
        return auth_user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                data['user'] = user
                return data
            else:
                raise serializers.ValidationError("Invalid login credentials!")
        else:
            raise serializers.ValidationError("Both email and password are required!")


class PasswordChangeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_email(self, value):
        user = self.context['request'].user
        if value != user.email:
            raise serializers.ValidationError("Invalid email for the provided token.")
        return value

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect!")
        return value

    def save(self):
        user = self.context['request'].user
        new_password = self.validated_data['new_password']
        user.set_password(new_password)
        user.save()
        return user


class UpdateRoleSerializer(serializers.Serializer):
    _id = serializers.UUIDField()
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)

    def validate_role(self, value):
        if value not in dict(User.ROLE_CHOICES):
            raise serializers.ValidationError("Invalid role!")
        return value

    def validate(self, data):
        _id = data.get('_id')
        try:
            user = User.objects.get(_id=_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this uid does not exist!")
        self.validate_permissions(user, self.context.get('request'))
        return data

    def validate_permissions(self, user, request):
        if request and request.user.role not in [User.ADMIN]:
            raise serializers.ValidationError("Only admins can update role!")
