import uuid
from django.db import models
from apps.appointments.models import Appointment


class Queue(models.Model):

    STATUS_CHOICES = [
        ("waiting", "Waiting"),
        ("active", "Active"),
        ("completed", "Completed"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="queue"
    )

    queue_number = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="waiting")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["queue_number"]

    def __str__(self):
        return f"Queue #{self.queue_number}"