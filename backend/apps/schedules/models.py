from django.db import models

from apps.doctors.models import Doctor


class DoctorSchedule(models.Model):

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="schedules"
    )

    day_of_week = models.IntegerField(
        choices=[
            (0, "Monday"),
            (1, "Tuesday"),
            (2, "Wednesday"),
            (3, "Thursday"),
            (4, "Friday"),
            (5, "Saturday"),
            (6, "Sunday"),
        ]
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    slot_duration_minutes = models.IntegerField(
        default=10
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.doctor.user.username} - Day {self.day_of_week}"
    
class DoctorAvailableSlot(models.Model):

    schedule = models.ForeignKey(
        DoctorSchedule,
        on_delete=models.CASCADE,
        related_name="slots"
    )

    start_datetime = models.DateTimeField()

    end_datetime = models.DateTimeField()

    is_booked = models.BooleanField(
        default=False
    )

    is_emergency_reserved = models.BooleanField(
        default=False
    )

    def __str__(self):

        return f"{self.schedule.doctor.user.username} Slot"