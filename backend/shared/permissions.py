from rest_framework.permissions import BasePermission

from shared.enums import UserRole


class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role == UserRole.SUPER_ADMIN
        )

class IsAuthenticated(BasePermission):

    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):

        return bool(
            request.user
            and request.user.is_authenticated
        )
    
class IsHospitalAdmin(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role == UserRole.HOSPITAL_ADMIN
        )


class IsStaff(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role == UserRole.STAFF
        )


class IsDoctor(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role == UserRole.DOCTOR
        )


class IsPatient(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role == UserRole.PATIENT
        )


class IsSuperAdminOrHospitalAdmin(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and request.user.role in [
                UserRole.SUPER_ADMIN,
                UserRole.HOSPITAL_ADMIN
            ]
        )


class IsStaffOrHospitalAdmin(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and request.user.role in [
                UserRole.STAFF,
                UserRole.HOSPITAL_ADMIN
            ]
        )


class IsDoctorOrHospitalAdmin(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and request.user.role in [
                UserRole.DOCTOR,
                UserRole.HOSPITAL_ADMIN
            ]
        )