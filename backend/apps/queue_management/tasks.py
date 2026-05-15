from celery import shared_task
from engine.queue_engine import QueueEngine


@shared_task
def recalc_queue_task(hospital_id, doctor_id):

    from apps.hospitals.models import Hospital
    from apps.doctors.models import Doctor

    # You can extend logic here later
    pass