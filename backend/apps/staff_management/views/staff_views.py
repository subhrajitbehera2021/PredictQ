from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.staff_management.models import Staff
from apps.staff_management.serializers.staff_serializers import StaffSerializer
from apps.staff_management.services.staff_services import StaffService
from apps.staff_management.permissions import IsHospitalAdminOrSuperAdmin


class StaffListCreateView(APIView):

    permission_classes = [IsHospitalAdminOrSuperAdmin]

    def get(self, request):

        staffs = Staff.objects.all()
        serializer = StaffSerializer(staffs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = StaffSerializer(data=request.data)

        if serializer.is_valid():
            staff = StaffService.create_staff(serializer.validated_data)
            return Response(
                StaffSerializer(staff).data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffDetailView(APIView):

    permission_classes = [IsHospitalAdminOrSuperAdmin]

    def get_object(self, pk):
        return Staff.objects.get(pk=pk)

    def get(self, request, pk):

        staff = self.get_object(pk)
        serializer = StaffSerializer(staff)

        return Response(serializer.data)

    def put(self, request, pk):

        staff = self.get_object(pk)
        serializer = StaffSerializer(staff, data=request.data)

        if serializer.is_valid():
            updated = StaffService.update_staff(staff, serializer.validated_data)
            return Response(StaffSerializer(updated).data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        staff = self.get_object(pk)
        StaffService.deactivate_staff(staff)

        return Response(
            {"message": "Staff deactivated"},
            status=status.HTTP_200_OK
        )