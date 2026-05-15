from django.contrib.auth import authenticate

from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import (
    RefreshToken
)

from shared.responses import (
    SuccessResponse,
    ErrorResponse
)


class LoginView(APIView):

    authentication_classes = []

    permission_classes = []

    def post(self, request):

        email = request.data.get(
            "email"
        )

        password = request.data.get(
            "password"
        )

        user = authenticate(
            username=email,
            password=password
        )

        if not user:

            return ErrorResponse(
                message="Invalid credentials",
                status=401
            )

        refresh = RefreshToken.for_user(
            user
        )

        return SuccessResponse(
            data={
                "access_token": str(
                    refresh.access_token
                ),
                "refresh_token": str(
                    refresh
                ),
                "user": {
                    "id": str(user.id),
                    "email": user.email,
                    "username": user.username,
                    "role": user.role
                }
            },
            message="Login successful"
        )