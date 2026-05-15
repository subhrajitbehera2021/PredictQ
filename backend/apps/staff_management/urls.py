from django.urls import path
from .views.staff_views import StaffListCreateView, StaffDetailView

urlpatterns = [
    path("", StaffListCreateView.as_view(), name="staff-list-create"),
    path("<int:pk>/", StaffDetailView.as_view(), name="staff-detail"),
]