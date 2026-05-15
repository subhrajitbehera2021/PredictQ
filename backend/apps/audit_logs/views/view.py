from rest_framework.views import APIView
from rest_framework.response import Response

from audit_logs.models import AuditLog
from audit_logs.serializers.serializer import AuditLogSerializer


class AuditLogListView(APIView):

    def get(self, request):

        logs = AuditLog.objects.all().order_by("-created_at")[:100]
        serializer = AuditLogSerializer(logs, many=True)

        return Response(serializer.data)