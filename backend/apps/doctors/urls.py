from django.urls import path

from apps.doctors.views.doctor_view import (
    DoctorListCreateView
)

from apps.doctors.views.doctor_detail_view import (
    DoctorDetailView
)


urlpatterns = [

    path(
        "",
        DoctorListCreateView.as_view(),
        name="doctor-list-create"
    ),

    path(
        "<int:doctor_id>/",
        DoctorDetailView.as_view(),
        name="doctor-detail"
    ),
]