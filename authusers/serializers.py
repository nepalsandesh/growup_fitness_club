from rest_framework import serializers
from authusers.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, data):
        return CustomUser.objects.create_user(**data)


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)