from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Patient
from .serializers import PatientSerializer

class PatientRegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Patient registered"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientLoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        return Response({
            "access": "patient_token",
            "refresh": "patient_refresh_token"
        })
    
class PatientListCreateView(APIView):

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        return get_object_or_404(Patient, id=id)

    def get(self, request, id):
        patient = self.get_object(id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, id):
        patient = self.get_object(id)
        serializer = PatientSerializer(patient, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        patient = self.get_object(id)
        patient.delete()

        return Response(
            {"message": "Patient deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
    
