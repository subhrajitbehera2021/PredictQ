from django.urls import path
from .views.analytics_view import (
    GenerateHospitalAnalyticsView,
    HospitalAnalyticsListView,
    GenerateDoctorAnalyticsView,
    DoctorAnalyticsListView
)

urlpatterns = [
    path("hospital/<int:hospital_id>/generate/", GenerateHospitalAnalyticsView.as_view()),
    path("hospital/<int:hospital_id>/", HospitalAnalyticsListView.as_view()),

    path("doctor/<int:doctor_id>/generate/", GenerateDoctorAnalyticsView.as_view()),
    path("doctor/<int:doctor_id>/", DoctorAnalyticsListView.as_view()),
]