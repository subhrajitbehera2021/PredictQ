from django.urls import path
from .views.view import NextPatientView, QueueView

app_name = "queue_management"

urlpatterns = [
    path("", QueueView.as_view(), name="queue-list"),
    path("next/", NextPatientView.as_view(), name="next-patient"),
    
]