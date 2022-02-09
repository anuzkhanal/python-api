from rest_framework import serializers
from authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "token",
        )
        read_only_field = ["token"]


class PasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
