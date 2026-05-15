from django.urls import path
from .views.register_view import RegisterView
from .views.login_view import LoginView
from .views.logout_view import LogoutView
from .views.me_view import MeView

urlpatterns = [
    path("me/", MeView.as_view()),
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
]