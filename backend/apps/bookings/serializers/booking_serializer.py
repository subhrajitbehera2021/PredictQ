from rest_framework import serializers

from apps.bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:

        model = Booking

        fields = (
            "id",
            "patient",
            "doctor",
            "slot",
            "queue_number",
            "status",
            "is_emergency",
            "booked_at",
        )

        read_only_fields = (
            "queue_number",
            "status",
            "booked_at",
        )