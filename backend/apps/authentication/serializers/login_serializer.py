from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class LoginView(APIView):

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)

            if not user.check_password(password):
                return Response({"error": "Invalid password"}, status=401)

            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": str(user.id),
                    "email": user.email,
                    "role": user.role,
                    "hospital": user.hospital_id
                }
            })

        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)