from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return Response({
            "id": str(user.id),
            "email": user.email,
            "username": user.username,
            "role": user.role,
            "hospital": str(user.hospital.id) if user.hospital else None
        })