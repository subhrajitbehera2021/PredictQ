from rest_framework.views import APIView

from apps.bookings.models import Booking
from apps.bookings.serializers.booking_serializer import BookingSerializer

from apps.bookings.services.services import BookingService

from apps.queue_management.services.queue_service import QueueService
from apps.queue_management.services.wait_time_service import WaitTimeService

from shared.responses import SuccessResponse, ErrorResponse


class BookingCreateView(APIView):

    def get(self, request):

        bookings = Booking.objects.select_related(
            "doctor",
            "patient",
            "slot"
        ).all().order_by("-booked_at")

        serializer = BookingSerializer(bookings, many=True)

        return SuccessResponse(
            data=serializer.data,
            message="Bookings fetched successfully"
        )

    def post(self, request):

        serializer = BookingSerializer(data=request.data)

        if not serializer.is_valid():

            return ErrorResponse(
                message="Validation Error",
                errors=serializer.errors
            )

        # -------------------------------
        # CREATE BOOKING
        # -------------------------------
        booking = BookingService.create_booking(
            patient=request.user,
            doctor=serializer.validated_data["doctor"],
            slot=serializer.validated_data["slot"],
            is_emergency=serializer.validated_data.get("is_emergency", False)
        )

        # -------------------------------
        # QUEUE LOGIC
        # -------------------------------
        position = QueueService.get_position(booking)

        wait_time = WaitTimeService.estimate_wait_time(position)

        # -------------------------------
        # RESPONSE DATA
        # -------------------------------
        data = {
            "booking": BookingSerializer(booking).data,
            "queue_position": position,
            "estimated_wait_time_minutes": wait_time
        }

        return SuccessResponse(
            data=data,
            message="Booking created successfully with queue info",
            status=201
        )