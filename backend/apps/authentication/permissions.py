from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "super_admin"
        )


class IsHospitalAdmin(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "hospital_admin"
        )


class IsDoctor(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "doctor"
        )


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "staff"
        )