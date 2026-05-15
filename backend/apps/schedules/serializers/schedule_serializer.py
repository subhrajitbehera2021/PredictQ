from rest_framework import serializers

from apps.schedules.models import DoctorSchedule


class DoctorScheduleSerializer(serializers.ModelSerializer):

    doctor_name = serializers.CharField(
        source="doctor.user.username",
        read_only=True
    )

    class Meta:

        model = DoctorSchedule

        fields = (
            "id",
            "doctor",
            "doctor_name",
            "day_of_week",
            "start_time",
            "end_time",
            "slot_duration_minutes",
            "is_active",
            "created_at",
        )

        read_only_fields = (
            "created_at",
        )