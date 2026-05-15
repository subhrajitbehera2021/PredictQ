from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "mobile",
        "age",
        "gender",
        "created_at",
    )

    search_fields = ("name", "email", "mobile")

    list_filter = ("gender",)