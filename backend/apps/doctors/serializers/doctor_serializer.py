from rest_framework import serializers

from apps.doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):

    doctor_name = serializers.CharField(
        source="user.username",
        read_only=True
    )

    hospital_name = serializers.CharField(
        source="hospital.name",
        read_only=True
    )

    department_name = serializers.CharField(
        source="department.name",
        read_only=True
    )

    class Meta:

        model = Doctor

        fields = (
            "id",
            "user",
            "doctor_name",
            "hospital",
            "hospital_name",
            "department",
            "department_name",
            "specialization",
            "experience_years",
            "license_number",
            "consultation_fee",
            "is_available",
            "is_on_duty",
            "created_at",
        )

        read_only_fields = (
            "created_at",
        )