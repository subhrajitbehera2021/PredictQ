from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from apps.hospitals.models import Hospital

from apps.hospitals.serializers.hospital_serializer import (
    HospitalSerializer,
)

from shared.responses import (
    SuccessResponse,
    ErrorResponse,
)


class HospitalDetailView(APIView):

    def get(self, request, hospital_id):

        hospital = get_object_or_404(
            Hospital,
            id=hospital_id
        )

        serializer = HospitalSerializer(
            hospital
        )

        return SuccessResponse(
            data=serializer.data,
            message="Hospital fetched successfully"
        )

    def put(self, request, hospital_id):

        hospital = get_object_or_404(
            Hospital,
            id=hospital_id
        )

        serializer = HospitalSerializer(
            hospital,
            data=request.data,
            partial=True
        )

        if not serializer.is_valid():

            return ErrorResponse(
                message="Validation Error",
                errors=serializer.errors,
            )

        serializer.save()

        return SuccessResponse(
            data=serializer.data,
            message="Hospital updated successfully"
        )

    def delete(self, request, hospital_id):

        hospital = get_object_or_404(
            Hospital,
            id=hospital_id
        )

        hospital.delete()

        return SuccessResponse(
            message="Hospital deleted successfully"
        )