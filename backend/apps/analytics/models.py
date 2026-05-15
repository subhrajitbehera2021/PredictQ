from django.db import models
from apps.hospitals.models import Hospital
from apps.doctors.models import Doctor
from apps.core.models import BaseUUIDModel


class HospitalAnalytics(BaseUUIDModel):

    id = models.BigAutoField(primary_key=True)

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name="analytics"
    )

    total_patients = models.IntegerField(default=0)
    total_bookings = models.IntegerField(default=0)
    total_emergency_cases = models.IntegerField(default=0)

    average_wait_time = models.FloatField(default=0.0)  # in minutes

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.hospital.name} - {self.date}"


class DoctorAnalytics(BaseUUIDModel):

    id = models.BigAutoField(primary_key=True)

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="analytics"
    )

    patients_seen = models.IntegerField(default=0)
    avg_consult_time = models.FloatField(default=0.0)
    total_hours_worked = models.FloatField(default=0.0)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor.user.username} - {self.date}"