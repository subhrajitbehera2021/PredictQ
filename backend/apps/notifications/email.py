from django.core.mail import send_mail
from django.conf import settings


class EmailService:

    @staticmethod
    def send(to_email, subject, message):

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [to_email],
            fail_silently=False
        )