from django.urls import re_path

from apps.queue_management.websocket.queue_consumer import QueueConsumer


websocket_urlpatterns = [

    re_path(
        r"ws/queue/(?P<doctor_id>\d+)/$",
        QueueConsumer.as_asgi()
    ),
]