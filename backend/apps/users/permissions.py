from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.is_super_admin
        )


class IsHospitalAdmin(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.is_hospital_admin
        )


class IsDoctor(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.is_doctor
        )


class IsStaffUser(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.is_staff_user
        )


class IsPatient(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.is_patient
        )


class IsSuperAdminOrHospitalAdmin(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and (
                request.user.is_super_admin
                or request.user.is_hospital_admin
            )
        )


class IsDoctorOrStaff(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and (
                request.user.is_doctor
                or request.user.is_staff_user
            )
        )


class IsHospitalRelatedUser(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role in [
                "hospital_admin",
                "doctor",
                "staff",
            ]
        )


class IsOwnerOrSuperAdmin(BasePermission):

    def has_object_permission(
        self,
        request,
        view,
        obj
    ):

        return (
            request.user.is_super_admin
            or obj == request.user
        )


class IsSameHospital(BasePermission):

    def has_object_permission(
        self,
        request,
        view,
        obj
    ):

        if request.user.is_super_admin:
            return True

        return (
            hasattr(obj, "hospital")
            and obj.hospital == request.user.hospital
        )