from apps.notifications.models import Notification
from apps.notifications.email import EmailService
from apps.notifications.sms import SMSService
from apps.notifications.whatsapp import WhatsAppService


class NotificationService:

    @staticmethod
    def send_email(user, title, message):

        EmailService.send(user.email, title, message)

        return Notification.objects.create(
            user=user,
            channel="EMAIL",
            title=title,
            message=message,
            status="SENT"
        )

    @staticmethod
    def send_sms(user, message):

        SMSService.send(user.phone, message)

        return Notification.objects.create(
            user=user,
            channel="SMS",
            title="SMS Notification",
            message=message,
            status="SENT"
        )

    @staticmethod
    def send_whatsapp(user, message):

        WhatsAppService.send(user.phone, message)

        return Notification.objects.create(
            user=user,
            channel="WHATSAPP",
            title="WhatsApp Notification",
            message=message,
            status="SENT"
        )