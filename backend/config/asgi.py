import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import apps.queue_management.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({

    "http": django_asgi_app,

    "websocket": URLRouter(
        apps.queue_management.routing.websocket_urlpatterns
    ),
})