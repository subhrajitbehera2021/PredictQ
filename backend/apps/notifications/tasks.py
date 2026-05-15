from celery import shared_task
from notifications.services.service import NotificationService


@shared_task
def send_email_task(user_id, title, message):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    user = User.objects.get(id=user_id)
    NotificationService.send_email(user, title, message)


@shared_task
def send_sms_task(user_id, message):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    user = User.objects.get(id=user_id)
    NotificationService.send_sms(user, message)


@shared_task
def send_whatsapp_task(user_id, message):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    user = User.objects.get(id=user_id)
    NotificationService.send_whatsapp(user, message)