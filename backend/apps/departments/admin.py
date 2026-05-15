from django.contrib import admin

from apps.departments.models import (
    Department
)


@admin.register(Department)
class DepartmentAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "name",
        "hospital",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
        "hospital",
    )