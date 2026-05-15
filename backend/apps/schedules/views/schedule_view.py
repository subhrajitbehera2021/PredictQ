from rest_framework.views import APIView

from apps.schedules.models import DoctorSchedule

from apps.schedules.serializers.schedule_serializer import (
    DoctorScheduleSerializer
)

from apps.schedules.services.services import ScheduleService

from shared.responses import (
    SuccessResponse,
    ErrorResponse,
)


class ScheduleListCreateView(APIView):

    def get(self, request):

        schedules = DoctorSchedule.objects.select_related(
            "doctor"
        ).all()

        serializer = DoctorScheduleSerializer(
            schedules,
            many=True
        )

        return SuccessResponse(
            data=serializer.data,
            message="Schedules fetched successfully"
        )

    def post(self, request):

        serializer = DoctorScheduleSerializer(
            data=request.data
        )

        if not serializer.is_valid():

            return ErrorResponse(
                message="Validation Error",
                errors=serializer.errors
            )

        schedule = serializer.save()

        ScheduleService.create_schedule(schedule)

        return SuccessResponse(
            data=serializer.data,
            message="Schedule created with slots",
            status=201
        )