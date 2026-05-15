from django.db import models
from apps.core.models import BaseUUIDModel
from apps.users.models import User
from apps.doctors.models import Doctor
from apps.schedules.models import DoctorAvailableSlot


class Booking(BaseUUIDModel):

    STATUS_CHOICES = (
        ("PENDING", "PENDING"),
        ("CONFIRMED", "CONFIRMED"),
        ("COMPLETED", "COMPLETED"),
        ("CANCELLED", "CANCELLED"),
        ("NO_SHOW", "NO_SHOW"),
    )

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    slot = models.ForeignKey(
        DoctorAvailableSlot,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    queue_number = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    is_emergency = models.BooleanField(
        default=False
    )

    booked_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.patient.username} - {self.doctor.user.username} - {self.queue_number}"