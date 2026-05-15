from apps.bookings.models import Booking


class QueueService:

    @staticmethod
    def get_active_queue(doctor, slot):

        return Booking.objects.filter(
            doctor=doctor,
            slot=slot,
            status="PENDING"
        ).order_by(
            "-is_emergency",
            "booked_at"
        )

    @staticmethod
    def get_position(booking):

        queue = Booking.objects.filter(
            doctor=booking.doctor,
            slot=booking.slot,
            status="PENDING"
        ).order_by(
            "-is_emergency",
            "booked_at"
        )

        for index, b in enumerate(queue, start=1):

            if b.id == booking.id:

                return index

        return None