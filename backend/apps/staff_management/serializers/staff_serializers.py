from rest_framework import serializers
from apps.staff_management.models import Staff


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = "__all__"
        read_only_fields = ["id", "joined_at", "updated_at"]