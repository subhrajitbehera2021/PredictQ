from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
from apps.notifications.services.service import NotificationService


User = get_user_model()


class SendEmailView(APIView):

    def post(self, request):

        user = User.objects.get(id=request.data["user_id"])

        notification = NotificationService.send_email(
            user,
            request.data["title"],
            request.data["message"]
        )

        return Response({"status": "email sent", "id": notification.id})


class SendSMSView(APIView):

    def post(self, request):

        user = User.objects.get(id=request.data["user_id"])

        notification = NotificationService.send_sms(
            user,
            request.data["message"]
        )

        return Response({"status": "sms sent", "id": notification.id})


class SendWhatsAppView(APIView):

    def post(self, request):

        user = User.objects.get(id=request.data["user_id"])

        notification = NotificationService.send_whatsapp(
            user,
            request.data["message"]
        )

        return Response({"status": "whatsapp sent", "id": notification.id})

class NotificationListView(APIView):
    def get(self, request):
        return Response({
            "message": "Notifications root working"
        })