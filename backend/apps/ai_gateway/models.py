from django.db import models
from apps.hospitals.models import Hospital
from django.conf import settings


class DecisionLog(models.Model):

    id = models.BigAutoField(primary_key=True)

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name="decision_logs"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    action_type = models.CharField(max_length=100)

    input_data = models.JSONField()

    output_data = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action_type