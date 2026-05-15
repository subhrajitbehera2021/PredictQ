from apps.bookings.models import Booking


class QueueEngine:

    @staticmethod
    def get_next_queue_number(doctor, slot):

        last_booking = Booking.objects.filter(
            doctor=doctor,
            slot=slot
        ).order_by("-queue_number").first()

        if last_booking:

            return last_booking.queue_number + 1

        return 1