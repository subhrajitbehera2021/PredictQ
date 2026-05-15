from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
User = get_user_model()
from apps.users.serializers.user_serializer import UserSerializer
from shared.responses import SuccessResponse


class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = UserSerializer(request.user)

        return SuccessResponse(
            data=serializer.data,
            message="Profile fetched successfully"
        )