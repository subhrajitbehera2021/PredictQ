from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from apps.queue_management.models import Queue
from apps.queue_management.serializers.serializer import QueueSerializer
from apps.queue_management.services.queue_service import QueueService

from apps.hospitals.models import Hospital
from apps.doctors.models import Doctor

from shared.responses import SuccessResponse, ErrorResponse
from shared.permissions import IsAuthenticated

class NextPatientView(APIView):

    def post(self, request):

        # get next waiting patient
        next_patient = Queue.objects.filter(status="waiting").order_by("queue_number").first()

        if not next_patient:
            return Response({"message": "No patients in queue"})

        # mark active
        next_patient.status = "active"
        next_patient.save()

        # mark others remain waiting
        return Response({
            "success": True,
            "queue_number": next_patient.queue_number,
            "appointment_id": next_patient.appointment.id,
            "status": "active"
        })

# --------------------------------------------------
# 📋 QUEUE LIST + CREATE
# --------------------------------------------------
class QueueView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        hospital_id = request.query_params.get("hospital_id")

        if not hospital_id:
            return Response(
                ErrorResponse("hospital_id is required"),
                status=status.HTTP_400_BAD_REQUEST
            )

        queues = Queue.objects.filter(
            hospital_id=hospital_id
        ).order_by("created_at")

        serializer = QueueSerializer(queues, many=True)

        return Response(
            SuccessResponse(serializer.data),
            status=status.HTTP_200_OK
        )

    def post(self, request):

        serializer = QueueSerializer(data=request.data)

        if serializer.is_valid():

            queue = serializer.save()

            # 🔥 Call business logic layer
            QueueService.process_new_queue(queue)

            return Response(
                SuccessResponse(serializer.data),
                status=status.HTTP_201_CREATED
            )

        return Response(
            ErrorResponse(serializer.errors),
            status=status.HTTP_400_BAD_REQUEST
        )


# --------------------------------------------------
# 📌 SINGLE QUEUE DETAIL
# --------------------------------------------------
class QueueDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        queue = get_object_or_404(Queue, id=pk)

        serializer = QueueSerializer(queue)

        return Response(
            SuccessResponse(serializer.data),
            status=status.HTTP_200_OK
        )


# --------------------------------------------------
# 🔄 UPDATE QUEUE STATUS (CALL / SKIP / COMPLETE)
# --------------------------------------------------
class QueueStatusUpdateView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        queue = get_object_or_404(Queue, id=pk)

        new_status = request.data.get("status")

        if not new_status:
            return Response(
                ErrorResponse("status is required"),
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔥 Business logic handled in service layer
        updated_queue = QueueService.update_queue_status(
            queue,
            new_status
        )

        serializer = QueueSerializer(updated_queue)

        return Response(
            SuccessResponse(serializer.data),
            status=status.HTTP_200_OK
        )


# --------------------------------------------------
# 🚨 EMERGENCY PRIORITY QUEUE INSERTION
# --------------------------------------------------
class EmergencyQueueView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        patient_id = request.data.get("patient_id")
        hospital_id = request.data.get("hospital_id")

        if not patient_id or not hospital_id:
            return Response(
                ErrorResponse("patient_id and hospital_id required"),
                status=status.HTTP_400_BAD_REQUEST
            )

        queue = QueueService.add_emergency_patient(
            patient_id=patient_id,
            hospital_id=hospital_id
        )

        serializer = QueueSerializer(queue)

        return Response(
            SuccessResponse(serializer.data),
            status=status.HTTP_201_CREATED
        )