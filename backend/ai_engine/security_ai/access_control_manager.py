from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class AccessControlManager:

    def __init__(self):

        self.roles = {

            "ADMIN": [
                "FULL_ACCESS",
                "MANAGE_DOCTORS",
                "VIEW_ANALYTICS",
                "MANAGE_SYSTEM"
            ],

            "DOCTOR": [
                "VIEW_PATIENTS",
                "UPDATE_PATIENT_STATUS"
            ],

            "RECEPTIONIST": [
                "REGISTER_PATIENT",
                "VIEW_QUEUE"
            ]
        }

    # =====================================================
    # VALIDATE ROLE
    # =====================================================

    def validate_role(
        self,
        role: str
    ):

        valid = role in self.roles

        logger.info(
            f"Role validation: "
            f"{role} -> {valid}"
        )

        return valid

    # =====================================================
    # GET ROLE PERMISSIONS
    # =====================================================

    def get_permissions(
        self,
        role: str
    ):

        permissions = self.roles.get(
            role,
            []
        )

        logger.info(
            f"Permissions fetched for "
            f"{role}"
        )

        return permissions

    # =====================================================
    # CHECK PERMISSION
    # =====================================================

    def has_permission(
        self,
        role: str,
        permission: str
    ):

        permissions = self.get_permissions(
            role
        )

        allowed = (
            permission in permissions
        )

        logger.info(
            f"Permission check: "
            f"{role} -> {permission} "
            f"= {allowed}"
        )

        return allowed

    # =====================================================
    # REGISTER NEW ROLE
    # =====================================================

    def register_role(
        self,
        role: str,
        permissions: list
    ):

        self.roles[role] = permissions

        logger.info(
            f"New role registered: "
            f"{role}"
        )

        return {
            "role": role,
            "permissions": permissions
        }

    # =====================================================
    # SYSTEM ACCESS REPORT
    # =====================================================

    def generate_access_report(self):

        report = {

            "total_roles":
            len(self.roles),

            "roles":
            self.roles
        }

        logger.info(
            "Access report generated"
        )

        return report