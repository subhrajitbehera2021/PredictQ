import uuid
from django.db import models
from apps.patients.models import Patient


class Appointment(models.Model):

    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('waiting', 'Waiting'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    doctor_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    token_number = models.CharField(max_length=50, unique=True)

    estimated_wait_time = models.PositiveIntegerField(default=0)
    queue_position = models.PositiveIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled'
    )

    ai_priority_score = models.FloatField(default=0)
    emergency_case = models.BooleanField(default=False)

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['appointment_date', 'appointment_time']

    def __str__(self):
        return f"{self.patient} - {self.token_number}"