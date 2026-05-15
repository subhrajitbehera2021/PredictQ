from ai_engine.engine import AIQueueEngine


class AIGatewayService:
    def __init__(self):
        self.engine = AIQueueEngine()

    def process_appointment(self, appointment):
        ai_input = {
            "appointment_id": str(appointment.id),
            "patient_id": str(appointment.patient.id),
            "patient_name": getattr(appointment.patient, "full_name", "Unknown Patient"),
            "doctor_name": appointment.doctor_name,
            "department": appointment.department,
            "appointment_date": str(appointment.appointment_date),
            "appointment_time": str(appointment.appointment_time),
            "emergency_case": appointment.emergency_case,
            "status": appointment.status,
        }

        # temporary AI logic until your AIQueueEngine method is confirmed
        priority_score = 0.9 if appointment.emergency_case else 0.5

        appointment.ai_priority_score = priority_score
        appointment.estimated_wait_time = 5 if appointment.emergency_case else 20
        appointment.queue_position = 1 if appointment.emergency_case else 3
        appointment.save()

        return appointment