from enum import Enum
from django.db import models


class UserRole(Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    HOSPITAL_ADMIN = "HOSPITAL_ADMIN"
    DOCTOR = "DOCTOR"
    STAFF = "STAFF"
    PATIENT = "PATIENT"



class UserRole(models.TextChoices):

    SUPER_ADMIN = "SUPER_ADMIN", "SUPER_ADMIN"

    HOSPITAL_ADMIN = "HOSPITAL_ADMIN", "HOSPITAL_ADMIN"

    STAFF = "STAFF", "STAFF"

    DOCTOR = "DOCTOR", "DOCTOR"

    PATIENT = "PATIENT", "PATIENT"