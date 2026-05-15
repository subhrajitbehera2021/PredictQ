from django.urls import path

from apps.bookings.views.booking_view import (
    BookingCreateView
)


urlpatterns = [

    path(
        "",
        BookingCreateView.as_view(),
        name="booking"
    ),

]