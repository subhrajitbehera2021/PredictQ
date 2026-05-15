from datetime import datetime, timedelta


def generate_slots(
    start_time,
    end_time,
    slot_duration
):

    slots = []

    current = datetime.combine(
        datetime.today(),
        start_time
    )

    end = datetime.combine(
        datetime.today(),
        end_time
    )

    while current + timedelta(
        minutes=slot_duration
    ) <= end:

        slot_start = current

        slot_end = current + timedelta(
            minutes=slot_duration
        )

        slots.append({
            "start": slot_start.time(),
            "end": slot_end.time(),
        })

        current = slot_end

    return slots