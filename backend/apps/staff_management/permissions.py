from rest_framework.permissions import BasePermission


class IsHospitalAdminOrSuperAdmin(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user or not user.is_authenticated:
            return False

        return (
            user.role == "SUPER_ADMIN"
            or user.role == "HOSPITAL_ADMIN"
        )


class IsStaffOrAbove(BasePermission):

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