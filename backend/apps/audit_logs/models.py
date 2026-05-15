from django.db import models
from django.conf import settings
from apps.hospitals.models import Hospital
from apps.core.models import BaseUUIDModel


class AuditLog(BaseUUIDModel):

    class ActionType(models.TextChoices):
        CREATE = "CREATE", "Create"
        UPDATE = "UPDATE", "Update"
        DELETE = "DELETE", "Delete"
        LOGIN = "LOGIN", "Login"
        LOGOUT = "LOGOUT", "Logout"
        ACCESS_DENIED = "ACCESS_DENIED", "Access Denied"
        SYSTEM = "SYSTEM", "System"

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="audit_logs"
    )

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs"
    )

    action = models.CharField(
        max_length=30,
        choices=ActionType.choices
    )

    model_name = models.CharField(max_length=100, blank=True, null=True)

    object_id = models.CharField(max_length=50, blank=True, null=True)

    message = models.TextField(blank=True, null=True)

    ip_address = models.GenericIPAddressField(null=True, blank=True)

    user_agent = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.user}"