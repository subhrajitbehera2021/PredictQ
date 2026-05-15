from django.contrib import admin
from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "role", "hospital", "department", "is_active")
    list_filter = ("role", "hospital", "is_active")
    search_fields = ("user__username", "role")