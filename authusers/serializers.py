from rest_framework.serializers import ModelSerializer
from authusers.models import CustomUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, data):
        return CustomUser.objects.create_user(**data)

    # def update(self, instance, validated_data):
    #     for key,value in validated_data.items():
    #         setattr(instance, key, value)
    #         instance.save()


from rest_framework import serializers
class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)