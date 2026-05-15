from django.urls import path
from .views import TestAIEngineView
from .views_f.view import ProcessAppointmentAIView

urlpatterns = [
    path("test-ai/", TestAIEngineView.as_view(), name="test-ai-engine"),
    path(
        "appointments/<uuid:appointment_id>/process-ai/",
        ProcessAppointmentAIView.as_view(),
        name="process-appointment-ai"
    ),
]