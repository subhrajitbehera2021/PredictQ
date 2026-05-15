from django.db import models
from django.conf import settings
from apps.core.models import BaseUUIDModel
from apps.hospitals.models import Hospital
from apps.departments.models import Department


class Staff(BaseUUIDModel):

    class StaffRole(models.TextChoices):
        NURSE = "NURSE", "Nurse"
        RECEPTIONIST = "RECEPTIONIST", "Receptionist"
        ASSISTANT = "ASSISTANT", "Assistant"
        PHARMACY = "PHARMACY", "Pharmacy Staff"
        LAB = "LAB", "Lab Staff"

    id = models.BigAutoField(primary_key=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="staff_profile"
    )

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name="staffs"
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="staffs"
    )

    role = models.CharField(
        max_length=20,
        choices=StaffRole.choices
    )

    phone = models.CharField(max_length=15, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    joined_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"