from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)



def health_check(request):
    return JsonResponse({
        "status": "QueueSenseAI API is running",
        "version": "v1"
    })

urlpatterns = [
    path('', health_check),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path(
        "api/v1/",
        include("config.api.v1.urls")
    ),

]