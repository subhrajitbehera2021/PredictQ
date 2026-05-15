from rest_framework import serializers
from apps.queue_management.models import Queue


class QueueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Queue
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "status"
        ]