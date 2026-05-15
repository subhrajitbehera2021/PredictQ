from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apps.patients.models import Patient
from .models import Appointment
from .serializers import AppointmentSerializer
from .services.queue_engine import create_appointment_with_queue
from apps.queue_management.models import Queue
from apps.queue_management.utils import generate_queue_number
from apps.ai_gateway.services import AIGatewayService


class CreateAppointmentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            patient = Patient.objects.get(user=request.user)
        except Patient.DoesNotExist:
            return Response(
                {"error": "Patient profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        data = request.data

        try:
            # 1. Create Appointment
            appointment = Appointment.objects.create(
                patient=patient,
                doctor_name=data.get("doctor_name"),
                department=data.get("department"),
                appointment_date=data.get("appointment_date"),
                appointment_time=data.get("appointment_time"),
                emergency_case=data.get("emergency_case", False),
                notes=data.get("notes"),
                token_number=f"TOKEN-{Appointment.objects.count() + 1}"
            )

            # 2. Create Queue
            queue = Queue.objects.create(
                appointment=appointment,
                queue_number=generate_queue_number(),
                status="waiting"
            )

            # 3. Run AI Gateway
            ai_gateway = AIGatewayService()
            appointment = ai_gateway.process_appointment(appointment)

            # 4. Refresh queue if AI changed queue fields
            queue.refresh_from_db()
            appointment.refresh_from_db()

            return Response({
                "success": True,
                "message": "Appointment created and processed by AI",
                "data": {
                    "appointment_id": appointment.id,
                    "token_number": appointment.token_number,
                    "queue_number": queue.queue_number,
                    "queue_status": queue.status,
                    "appointment_status": appointment.status,
                    "ai_priority_score": appointment.ai_priority_score,
                    "estimated_wait_time": appointment.estimated_wait_time,
                    "queue_position": appointment.queue_position,
                    "emergency_case": appointment.emergency_case
                }
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AppointmentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        appointments = Appointment.objects.all().order_by("-created_at")
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            patient = Patient.objects.get(user=request.user)

            # 1. Create appointment using existing queue service
            appointment = create_appointment_with_queue(
                request.data,
                patient
            )

            # 2. Run AI Gateway
            ai_gateway = AIGatewayService()
            appointment = ai_gateway.process_appointment(appointment)

            # 3. Return updated appointment
            serializer = AppointmentSerializer(appointment)

            return Response(
                {
                    "success": True,
                    "message": "Appointment created and processed by AI",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        except Patient.DoesNotExist:
            return Response(
                {"error": "Patient not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )