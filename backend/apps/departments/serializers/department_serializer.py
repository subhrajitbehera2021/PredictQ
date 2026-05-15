from rest_framework import serializers

from apps.departments.models import Department


class DepartmentSerializer(
    serializers.ModelSerializer
):

    hospital_name = serializers.CharField(
        source="hospital.name",
        read_only=True
    )

    class Meta:

        model = Department

        fields = (
            "id",
            "hospital",
            "hospital_name",
            "name",
            "description",
            "is_active",
            "created_at",
        )

        read_only_fields = (
            "created_at",
        )