from django.db import models
from apps.core.models import BaseUUIDModel
from apps.users.models import User
from apps.hospitals.models import Hospital
from apps.departments.models import Department


class Doctor(BaseUUIDModel):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name="doctors"
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="doctors"
    )

    specialization = models.CharField(
        max_length=255
    )

    experience_years = models.PositiveIntegerField(
        default=0
    )

    license_number = models.CharField(
        max_length=100,
        unique=True
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    is_available = models.BooleanField(
        default=True
    )

    is_on_duty = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return f"Dr. {self.user.username} - {self.specialization}"