from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.appointments.models import Appointment
from apps.ai_gateway.services import AIGatewayService


class TestAIEngineView(APIView):
    permission_classes = []

    def get(self, request):
        return Response({
            "success": True,
            "message": "AI Gateway is working. Use POST with appointment_id to process real appointment data."
        })

    def post(self, request):
        try:
            appointment_id = request.data.get("appointment_id")

            if not appointment_id:
                return Response({
                    "success": False,
                    "error": "appointment_id is required"
                }, status=status.HTTP_400_BAD_REQUEST)

            appointment = Appointment.objects.get(id=appointment_id)

            ai_gateway = AIGatewayService()
            updated_appointment = ai_gateway.process_appointment(appointment)

            return Response({
                "success": True,
                "message": "Real appointment processed by AI successfully",
                "data": {
                    "appointment_id": str(updated_appointment.id),
                    "patient_id": str(updated_appointment.patient.id),
                    "patient_name": getattr(updated_appointment.patient, "full_name", "Unknown Patient"),
                    "doctor_name": updated_appointment.doctor_name,
                    "department": updated_appointment.department,
                    "appointment_date": updated_appointment.appointment_date,
                    "appointment_time": updated_appointment.appointment_time,
                    "token_number": updated_appointment.token_number,
                    "status": updated_appointment.status,
                    "emergency_case": updated_appointment.emergency_case,
                    "ai_priority_score": updated_appointment.ai_priority_score,
                    "estimated_wait_time": updated_appointment.estimated_wait_time,
                    "queue_position": updated_appointment.queue_position,
                }
            }, status=status.HTTP_200_OK)

        except Appointment.DoesNotExist:
            return Response({
                "success": False,
                "error": "Appointment not found"
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProcessAppointmentAIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, appointment_id):
        try:
            appointment = Appointment.objects.get(id=appointment_id)

            ai_gateway = AIGatewayService()
            updated_appointment = ai_gateway.process_appointment(appointment)

            return Response({
                "success": True,
                "message": "Appointment AI processing completed",
                "data": {
                    "appointment_id": str(updated_appointment.id),
                    "token_number": updated_appointment.token_number,
                    "ai_priority_score": updated_appointment.ai_priority_score,
                    "estimated_wait_time": updated_appointment.estimated_wait_time,
                    "queue_position": updated_appointment.queue_position,
                    "emergency_case": updated_appointment.emergency_case,
                    "status": updated_appointment.status,
                }
            }, status=status.HTTP_200_OK)

        except Appointment.DoesNotExist:
            return Response({
                "success": False,
                "error": "Appointment not found"
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)