from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.ai_gateway.services import AIGatewayService
import traceback

class TestAIEngineView(APIView):
    permission_classes = []

    def get(self, request):
        return Response({
            "success": True,
            "message": "AI Gateway URL working. Use POST to test AI engine."
        })

    def post(self, request):
        try:
            ai_gateway = AIGatewayService()

            test_data = {
                "appointment_id": "test-001",
                "patient_id": "patient-001",
                "patient_name": request.data.get("patient_name", "Test Patient"),
                "doctor_name": request.data.get("doctor_name", "Dr. Sharma"),
                "department": request.data.get("department", "Cardiology"),
                "appointment_date": request.data.get("appointment_date", "2026-05-14"),
                "appointment_time": request.data.get("appointment_time", "10:30:00"),
                "emergency_case": request.data.get("emergency_case", False),
                "status": request.data.get("status", "scheduled"),
            }

            result = ai_gateway.process_test_data(test_data)

            return Response({
                "success": True,
                "input": test_data,
                "ai_result": result
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e),
                "traceback": traceback.format_exc()
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)