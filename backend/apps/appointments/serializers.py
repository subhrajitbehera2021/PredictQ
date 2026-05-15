from rest_framework import serializers

from .models import Patient
from apps.appointments.models import Appointment



class AppointmentSerializer(serializers.ModelSerializer):

    patient_name = serializers.CharField(
        source='patient.name',
        read_only=True
    )

    class Meta:
        model = Appointment

        fields = [
            "id",
            "patient",
            "patient_name",
            "doctor_name",
            "department",
            "appointment_date",
            "appointment_time",
            "token_number",
            "estimated_wait_time",
            "queue_position",
            "status",
            "ai_priority_score",
            "emergency_case",
            "notes",
            "created_at",
            "updated_at"
        ]

        read_only_fields = [
            "patient",
            "queue_position",
            "token_number",
            "created_at",
            "updated_at"
        ]