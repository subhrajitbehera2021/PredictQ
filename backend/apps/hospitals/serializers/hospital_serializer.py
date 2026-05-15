from rest_framework import serializers

from apps.hospitals.models import Hospital


class HospitalSerializer(serializers.ModelSerializer):

    hospital_admin_name = serializers.CharField(
        source="hospital_admin.username",
        read_only=True
    )

    class Meta:

        model = Hospital

        fields = (
            "id",
            "name",
            "slug",
            "email",
            "phone_number",
            "address",
            "city",
            "state",
            "country",
            "postal_code",
            "logo",
            "description",
            "hospital_admin",
            "hospital_admin_name",
            "is_active",
            "created_at",
        )

        read_only_fields = (
            "created_at",
        )