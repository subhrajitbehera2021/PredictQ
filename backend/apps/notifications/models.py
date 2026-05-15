from django.db import models
from django.conf import settings
from apps.core.models import BaseUUIDModel


class Notification(BaseUUIDModel):

    class Channel(models.TextChoices):
        EMAIL = "EMAIL", "Email"
        SMS = "SMS", "SMS"
        WHATSAPP = "WHATSAPP", "WhatsApp"
        PUSH = "PUSH", "Push Notification"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        SENT = "SENT", "Sent"
        FAILED = "FAILED", "Failed"

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    channel = models.CharField(
        max_length=20,
        choices=Channel.choices
    )

    title = models.CharField(max_length=255)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    sent_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.channel} - {self.user.username}"