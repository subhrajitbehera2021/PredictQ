from django.contrib import admin
from django.urls import include, path



urlpatterns = [

    path('admin/', admin.site.urls),

    path(
        "users/",
        include("apps.users.urls")
    ),
    
    path(
        "auth/",
        include("apps.authentication.urls")
    ),

    path(
        "hospitals/",
        include("apps.hospitals.urls")
    ),

    path(
        "departments/",
        include("apps.departments.urls")
    ),

    path(
        "doctors/",
        include("apps.doctors.urls")
    ),

    path(
        "schedules/",
        include("apps.schedules.urls")
    ),

    path(
        "bookings/",
        include("apps.bookings.urls")
    ),

    path(
        "queue-management/",
        include("apps.queue_management.urls")
    ),

    path(
        "staff-management/",
        include("apps.staff_management.urls")   
    ),

    path(
        "notifications/",
        include("apps.notifications.urls")
    ),

    path(
        "analytics/",
        include("apps.analytics.urls")
    ),

    path(
        'patients/',
        include('apps.patients.urls')
    ),

    path(
        'appointments/',
        include('apps.appointments.urls')
    ),

    path(
        "ai_gateway/",
        include("apps.ai_gateway.urls")
    ),
]