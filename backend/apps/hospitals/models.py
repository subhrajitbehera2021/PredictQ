from django.db import models
from apps.users.models import User
from apps.core.models import BaseUUIDModel


class Hospital(BaseUUIDModel):

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    country = models.CharField(max_length=100, default="India")
    postal_code = models.CharField(max_length=20)

    logo = models.ImageField(upload_to="hospitals/logo/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    hospital_admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="managed_hospitals"
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name