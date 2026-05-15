from rest_framework.permissions import BasePermission


class IsHospitalStaff(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user or not user.is_authenticated:
            return False

        return user.role in [
            "SUPER_ADMIN",
            "HOSPITAL_ADMIN",
            "DOCTOR",
            "STAFF"
        ]


class IsPatientOrStaff(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        return user.is_authenticated