from apps.audit_logs.models import AuditLog


class AuditLogService:

    @staticmethod
    def log(
        user=None,
        hospital=None,
        action=None,
        model_name=None,
        object_id=None,
        message=None,
        request=None
    ):

        ip = None
        user_agent = None

        if request:
            ip = request.META.get("REMOTE_ADDR")
            user_agent = request.META.get("HTTP_USER_AGENT")

        return AuditLog.objects.create(
            user=user,
            hospital=hospital,
            action=action,
            model_name=model_name,
            object_id=object_id,
            message=message,
            ip_address=ip,
            user_agent=user_agent
        )