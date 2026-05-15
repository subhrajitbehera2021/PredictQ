from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.hospitals.models import Hospital
from apps.doctors.models import Doctor

from apps.analytics.models import HospitalAnalytics, DoctorAnalytics
from apps.analytics.serializers.analytics_serializer import (
    HospitalAnalyticsSerializer,
    DoctorAnalyticsSerializer
)
from apps.analytics.services.service import AnalyticsService


class GenerateHospitalAnalyticsView(APIView):

    def post(self, request, hospital_id):

        try:
            hospital = Hospital.objects.get(id=hospital_id)
            analytics = AnalyticsService.generate_hospital_analytics(hospital)

            return Response(
                HospitalAnalyticsSerializer(analytics).data,
                status=status.HTTP_201_CREATED
            )

        except Hospital.DoesNotExist:
            return Response(
                {"error": "Hospital not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class HospitalAnalyticsListView(APIView):

    def get(self, request, hospital_id):

        analytics = HospitalAnalytics.objects.filter(hospital_id=hospital_id)
        serializer = HospitalAnalyticsSerializer(analytics, many=True)

        return Response(serializer.data)


class GenerateDoctorAnalyticsView(APIView):

    def post(self, request, doctor_id):

        try:
            doctor = Doctor.objects.get(id=doctor_id)
            analytics = AnalyticsService.generate_doctor_analytics(doctor)

            return Response(
                DoctorAnalyticsSerializer(analytics).data,
                status=status.HTTP_201_CREATED
            )

        except Doctor.DoesNotExist:
            return Response(
                {"error": "Doctor not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class DoctorAnalyticsListView(APIView):

    def get(self, request, doctor_id):

        analytics = DoctorAnalytics.objects.filter(doctor_id=doctor_id)
        serializer = DoctorAnalyticsSerializer(analytics, many=True)

        return Response(serializer.data)