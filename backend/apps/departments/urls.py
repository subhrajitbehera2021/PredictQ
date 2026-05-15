from django.urls import path

from apps.departments.views.department_view import (
    DepartmentListCreateView
)

from apps.departments.views.department_detail_view import (
    DepartmentDetailView
)


urlpatterns = [

    path(
        "",
        DepartmentListCreateView.as_view(),
        name="department-list-create",
    ),

    path(
        "<int:department_id>/",
        DepartmentDetailView.as_view(),
        name="department-detail",
    ),
]