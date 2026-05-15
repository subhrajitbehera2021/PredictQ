from apps.schedules.models import (
    DoctorSchedule,
    DoctorAvailableSlot
)

from apps.schedules.scheduler.slot_generator import (
    generate_slots
)

from datetime import datetime


class ScheduleService:

    @staticmethod
    def create_schedule(schedule):

        slots = generate_slots(
            schedule.start_time,
            schedule.end_time,
            schedule.slot_duration_minutes
        )

        for slot in slots:

            DoctorAvailableSlot.objects.create(

                schedule=schedule,

                start_datetime=datetime.combine(
                    datetime.today(),
                    slot["start"]
                ),

                end_datetime=datetime.combine(
                    datetime.today(),
                    slot["end"]
                ),
            )