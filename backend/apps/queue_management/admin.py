from django.contrib import admin
from .models import Queue


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "token_number",
        "hospital__name",
        "doctor__name",
    )


    readonly_fields = (
        "id",
        "created_at",
    )

    list_per_page = 25