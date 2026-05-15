from django.urls import path

from .views.hospital_view import (
    HospitalListCreateView,
)

from .views.hospital_detail_view import (
    HospitalDetailView,
)


urlpatterns = [

    path(
        "",
        HospitalListCreateView.as_view(),
        name="hospital-list-create",
    ),

    path(
        "<int:hospital_id>/",
        HospitalDetailView.as_view(),
        name="hospital-detail",
    ),
]