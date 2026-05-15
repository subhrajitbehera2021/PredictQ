from django.urls import path

from apps.users.views.user_view import ProfileView


urlpatterns = [

    path(
        "profile/",
        ProfileView.as_view(),
        name="profile"
    ),
]