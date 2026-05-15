from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.authentication.serializers.register_serializer import RegisterSerializer
from apps.patients.models import Patient


class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # ✅ Create User
        user = serializer.save()

        # ✅ Auto-create Patient safely (no duplicates)
        Patient.objects.get_or_create(
            user=user,
            defaults={
                "name": user.username
            }
        )

        return Response(
            {
                "message": "User created successfully",
                "user_id": str(user.id)
            },
            status=status.HTTP_201_CREATED
        )