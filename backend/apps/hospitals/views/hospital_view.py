from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.hospitals.models import Hospital
from apps.hospitals.serializers.hospital_serializer import HospitalSerializer
from apps.hospitals.services.service import HospitalService
from apps.hospitals.permissions import IsSuperAdminOrHospitalAdmin


class HospitalListCreateView(APIView):

    permission_classes = [IsSuperAdminOrHospitalAdmin]

    def get(self, request):

        hospitals = Hospital.objects.filter(is_active=True)
        serializer = HospitalSerializer(hospitals, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = HospitalSerializer(data=request.data)

        if serializer.is_valid():

            hospital = HospitalService.create_hospital(
                serializer.validated_data,
                request.user
            )

            return Response(
                HospitalSerializer(hospital).data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalDetailView(APIView):

    permission_classes = [IsSuperAdminOrHospitalAdmin]

    def get_object(self, identifier):

        # supports both ID and slug (IMPORTANT FOR REAL SYSTEMS)
        return Hospital.objects.filter(
            models.Q(id=identifier) | models.Q(slug=identifier)
        ).first()

    def get(self, request, identifier):

        hospital = self.get_object(identifier)

        if not hospital:
            return Response({"error": "Not found"}, status=404)

        serializer = HospitalSerializer(hospital)
        return Response(serializer.data)

    def put(self, request, identifier):

        hospital = self.get_object(identifier)

        if not hospital:
            return Response({"error": "Not found"}, status=404)

        serializer = HospitalSerializer(hospital, data=request.data)

        if serializer.is_valid():

            updated = HospitalService.update_hospital(
                hospital,
                serializer.validated_data
            )

            return Response(HospitalSerializer(updated).data)

        return Response(serializer.errors)

    def delete(self, request, identifier):

        hospital = self.get_object(identifier)

        if not hospital:
            return Response({"error": "Not found"}, status=404)

        HospitalService.deactivate_hospital(hospital)

        return Response(
            {"message": "Hospital deactivated"},
            status=status.HTTP_200_OK
        )