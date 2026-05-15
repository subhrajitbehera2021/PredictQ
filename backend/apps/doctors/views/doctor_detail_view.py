from django.shortcuts import get_object_or_404

from rest_framework.views import APIView

from apps.doctors.models import Doctor

from apps.doctors.serializers.doctor_serializer import (
    DoctorSerializer
)

from shared.responses import (
    SuccessResponse,
    ErrorResponse,
)


class DoctorDetailView(APIView):

    def get(self, request, doctor_id):

        doctor = get_object_or_404(
            Doctor,
            id=doctor_id
        )

        serializer = DoctorSerializer(
            doctor
        )

        return SuccessResponse(
            data=serializer.data,
            message="Doctor fetched successfully"
        )

    def put(self, request, doctor_id):

        doctor = get_object_or_404(
            Doctor,
            id=doctor_id
        )

        serializer = DoctorSerializer(
            doctor,
            data=request.data,
            partial=True
        )

        if not serializer.is_valid():

            return ErrorResponse(
                message="Validation Error",
                errors=serializer.errors
            )

        serializer.save()

        return SuccessResponse(
            data=serializer.data,
            message="Doctor updated successfully"
        )

    def delete(self, request, doctor_id):

        doctor = get_object_or_404(
            Doctor,
            id=doctor_id
        )

        doctor.delete()

        return SuccessResponse(
            message="Doctor deleted successfully"
        )