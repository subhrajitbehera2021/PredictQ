from .services.service import AuditLogService


class AuditLogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        user = getattr(request, "user", None)

        if user and user.is_authenticated:

            AuditLogService.log(
                user=user,
                action="SYSTEM",
                message=f"{request.method} {request.path}",
                request=request
            )

        return response