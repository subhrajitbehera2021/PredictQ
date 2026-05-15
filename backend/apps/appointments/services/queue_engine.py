import uuid
from django.db import transaction
from apps.appointments.models import Appointment

def generate_token():
    return f"T-{uuid.uuid4().hex[:10]}"

def get_next_queue_position(department, date):
    last = Appointment.objects.filter(
        department=department,
        appointment_date=date
    ).order_by("-queue_position").first()

    if last and last.queue_position:
        return last.queue_position + 1

    return 1

def rebuild_queue(department, date):

    appointments = Appointment.objects.filter(
        department=department,
        appointment_date=date,
        status__in=["scheduled", "waiting"]
    ).order_by(
        "-emergency_case",
        "-ai_priority_score",
        "appointment_time"
    )

    with transaction.atomic():
        position = 1

        for app in appointments:
            app.queue_position = position
            app.save(update_fields=["queue_position"])
            position += 1

def create_appointment_with_queue(data, patient):

    appointment = Appointment.objects.create(
        patient=patient,
        doctor_name=data["doctor_name"],
        department=data["department"],
        appointment_date=data["appointment_date"],
        appointment_time=data["appointment_time"],
        token_number=generate_token(),
        ai_priority_score=data.get("ai_priority_score", 0),
        emergency_case=data.get("emergency_case", False),
        queue_position=0
    )

    # assign queue position
    appointment.queue_position = get_next_queue_position(
        appointment.department,
        appointment.appointment_date
    )

    appointment.save()

    # reorder full queue
    rebuild_queue(
        appointment.department,
        appointment.appointment_date
    )

    return appointment

