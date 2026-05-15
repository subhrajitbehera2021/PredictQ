import time
import logging

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """
    Logs every request with execution time.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time

        logger.info(
            f"{request.method} {request.path} - {response.status_code} - {duration:.3f}s"
        )

        return response


class ActiveUserMiddleware:
    """
    Attaches user info safely to request context.
    Prevents crashes if user is anonymous.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request.user_role = None

        if request.user.is_authenticated:
            request.user_role = getattr(request.user, "role", None)

        return self.get_response(request)