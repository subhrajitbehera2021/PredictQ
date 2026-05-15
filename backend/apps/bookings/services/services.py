from apps.bookings.models import Booking

from apps.queue_management.engine.queue_engine import (
    QueueEngine
)


class BookingService:

    @staticmethod
    def create_booking(
        patient,
        doctor,
        slot,
        is_emergency=False
    ):

        queue_number = QueueEngine.get_next_queue_number(
            doctor,
            slot
        )

        booking = Booking.objects.create(
            patient=patient,
            doctor=doctor,
            slot=slot,
            queue_number=queue_number,
            is_emergency=is_emergency
        )

        return booking