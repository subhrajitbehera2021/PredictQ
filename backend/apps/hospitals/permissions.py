from rest_framework.permissions import BasePermission


class IsSuperAdminOrHospitalAdmin(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user or not user.is_authenticated:
            return False

        return user.role in ["SUPER_ADMIN", "HOSPITAL_ADMIN"]


class IsHospitalOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        user = request.user

        return (
            user.role == "SUPER_ADMIN"
            or obj.hospital_admin == user
        )