from django.urls import path
from .views import AppointmentListCreateView, CreateAppointmentView

urlpatterns = [
    path("", AppointmentListCreateView.as_view()),
    path("create/", CreateAppointmentView.as_view()),
]