from django.urls import path

from apps.schedules.views.schedule_view import (
    ScheduleListCreateView
)


urlpatterns = [

    path(
        "",
        ScheduleListCreateView.as_view(),
        name="schedule-list-create"
    ),

]