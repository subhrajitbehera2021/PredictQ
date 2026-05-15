from django.shortcuts import (
    get_object_or_404
)

from rest_framework.views import APIView

from apps.departments.models import (
    Department
)

from apps.departments.serializers.department_serializer import (
    DepartmentSerializer
)

from shared.responses import (
    SuccessResponse,
    ErrorResponse,
)


class DepartmentDetailView(
    APIView
):

    def get(self, request, department_id):

        department = get_object_or_404(
            Department,
            id=department_id
        )

        serializer = DepartmentSerializer(
            department
        )

        return SuccessResponse(
            data=serializer.data,
            message="Department fetched successfully"
        )

    def put(self, request, department_id):

        department = get_object_or_404(
            Department,
            id=department_id
        )

        serializer = DepartmentSerializer(
            department,
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
            message="Department updated successfully"
        )

    def delete(self, request, department_id):

        department = get_object_or_404(
            Department,
            id=department_id
        )

        department.delete()

        return SuccessResponse(
            message="Department deleted successfully"
        )