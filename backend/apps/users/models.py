import uuid

from django.db import models

from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(
        self,
        email,
        username,
        password=None,
        **extra_fields
    ):

        if not email:

            raise ValueError(
                "Email is required"
            )

        if not username:

            raise ValueError(
                "Username is required"
            )

        email = self.normalize_email(
            email
        )

        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )

        user.set_password(password)

        user.save(
            using=self._db
        )

        return user

    def create_superuser(
        self,
        email,
        username,
        password=None,
        **extra_fields
    ):

        extra_fields.setdefault(
            "is_staff",
            True
        )

        extra_fields.setdefault(
            "is_superuser",
            True
        )

        extra_fields.setdefault(
            "is_active",
            True
        )

        extra_fields.setdefault(
            "role",
            User.Roles.SUPER_ADMIN
        )

        return self.create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields
        )


class User(AbstractUser):

    class Roles(models.TextChoices):

        SUPER_ADMIN = (
            "super_admin",
            "Super Admin"
        )

        HOSPITAL_ADMIN = (
            "hospital_admin",
            "Hospital Admin"
        )

        DOCTOR = (
            "doctor",
            "Doctor"
        )

        STAFF = (
            "staff",
            "Staff"
        )

        PATIENT = (
            "patient",
            "Patient"
        )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    username = models.CharField(
        max_length=150,
        unique=True
    )

    email = models.EmailField(
        unique=True
    )

    role = models.CharField(
        max_length=30,
        choices=Roles.choices,
        default=Roles.PATIENT
    )

    hospital = models.ForeignKey(
        "hospitals.Hospital",
        on_delete=models.SET_NULL,
        related_name="users",
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    profile_image = models.ImageField(
        upload_to="users/profile/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "username"
    ]

    objects = UserManager()

    class Meta:

        db_table = "users"

        ordering = [
            "-created_at"
        ]

    def __str__(self):

        return self.email