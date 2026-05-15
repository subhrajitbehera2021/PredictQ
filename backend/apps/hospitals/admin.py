from django.contrib import admin

from apps.hospitals.models import Hospital


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "city",
        "state",
        "hospital_admin",
        "is_active",
    )

    search_fields = (
        "name",
        "city",
        "state",
    )

    list_filter = (
        "is_active",
        "state",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }