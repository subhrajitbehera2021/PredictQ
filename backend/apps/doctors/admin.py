from django.contrib import admin

from apps.doctors.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "hospital",
        "department",
        "specialization",
        "is_available",
        "is_on_duty",
    )

    list_filter = (
        "is_available",
        "is_on_duty",
        "hospital",
    )

    search_fields = (
        "user__username",
        "specialization",
    )

    autocomplete_fields = (
        "user",
        "hospital",
        "department",
    )