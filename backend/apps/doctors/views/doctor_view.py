from rest_framework.views import APIView

from apps.doctors.models import Doctor

from apps.doctors.serializers.doctor_serializer import (
    DoctorSerializer
)

from shared.responses import (
    SuccessResponse,
    ErrorResponse,
)


class DoctorListCreateView(APIView):

    def get(self, request):

        doctors = Doctor.objects.select_related(
            "user",
            "hospital",
            "department"
        ).all()

        serializer = DoctorSerializer(
            doctors,
            many=True
        )

        return SuccessResponse(
            data=serializer.data,
            message="Doctors fetched successfully"
        )

    def post(self, request):

        serializer = DoctorSerializer(
            data=request.data
        )

        if not serializer.is_valid():

            return ErrorResponse(
                message="Validation Error",
                errors=serializer.errors
            )

        serializer.save()

        return SuccessResponse(
            data=serializer.data,
            message="Doctor created successfully",
            status=201
        )