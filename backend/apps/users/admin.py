from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = (
        "email",
        "username",
        "role",
        "is_active",
        "created_at",
    )

    list_filter = (
        "role",
        "is_active",
    )

    search_fields = (
        "email",
        "username",
    )

    ordering = (
        "-created_at",
    )