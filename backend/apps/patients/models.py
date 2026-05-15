import uuid
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Patient(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=20)

    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)

    disease = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name