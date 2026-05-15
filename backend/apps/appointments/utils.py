from .models import Appointment


def generate_token():

    total = Appointment.objects.count() + 1

    return f"A-{total:03}"