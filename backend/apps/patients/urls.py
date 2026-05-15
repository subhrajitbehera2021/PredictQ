from django.urls import path

from .views import (
    PatientListCreateView,
    PatientDetailView,
    PatientRegisterView,
    PatientLoginView,
)

urlpatterns = [

    path(
        '',
        PatientListCreateView.as_view()
    ),

    path(
        'register/',
        PatientRegisterView.as_view()
    ),

    path(
        'login/',
        PatientLoginView.as_view()
    ),

    path(
        '<uuid:id>/',
        PatientDetailView.as_view()
    ),

]