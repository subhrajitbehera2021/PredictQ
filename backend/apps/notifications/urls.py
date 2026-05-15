from django.urls import path
from .views.view import (
    NotificationListView,
    SendEmailView,
    SendSMSView,
    SendWhatsAppView
)

urlpatterns = [
    path("email/", SendEmailView.as_view()),
    path("sms/", SendSMSView.as_view()),
    path("whatsapp/", SendWhatsAppView.as_view()),
    path("", NotificationListView.as_view()),
]