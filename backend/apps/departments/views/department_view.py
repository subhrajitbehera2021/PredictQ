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


class DepartmentListCreateView(
    APIView
):

    def get(self, request):

        departments = Department.objects.select_related(
            "hospital"
        ).all()

        serializer = DepartmentSerializer(
            departments,
            many=True
        )

        return SuccessResponse(
            data=serializer.data,
            message="Departments fetched successfully"
        )

    def post(self, request):

        serializer = DepartmentSerializer(
            data=request.data
        )

        if not serializer.is_valid():

            return ErrorResponse(
                message="Validation Error",
                errors=serializer.errors,
            )

        serializer.save()

        return SuccessResponse(
            data=serializer.data,
            message="Department created successfully",
            status=201,
        )