from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'patient',
        'doctor_name',
        'department',
        'token_number',
        'status',
    )

    search_fields = (
        'token_number',
        'doctor_name',
    )

    list_filter = (
        'status',
        'department',
    )