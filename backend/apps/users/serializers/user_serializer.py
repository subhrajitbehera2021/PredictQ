from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            "id",
            "username",
            "email",
            "role",
            "phone_number",
            "profile_image",
            "is_verified",
        )