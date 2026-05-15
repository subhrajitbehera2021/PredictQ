from apps.queue_management.engine.queue_engine import QueueEngine
from apps.emergency.engine.priority_engine import calculate_emergency_priority
from apps.notifications.services import NotificationService


class AIGatewayEngine:

    @staticmethod
    def handle_booking(booking):

        # 1. Check emergency
        priority = calculate_emergency_priority(booking)

        # 2. Add to queue
        queue = QueueEngine.add_to_queue(
            booking=booking,
            hospital=booking.hospital,
            doctor=booking.doctor
        )

        # 3. Notify user
        NotificationService.send_sms(
            booking.patient,
            f"Your token is {queue.token_number}"
        )

        return {
            "queue_id": queue.id,
            "token": queue.token_number,
            "priority": priority
        }

    @staticmethod
    def handle_emergency(booking):

        queue = QueueEngine.add_to_queue(
            booking=booking,
            hospital=booking.hospital,
            doctor=booking.doctor
        )

        queue.priority += 100
        queue.save()

        NotificationService.send_sms(
            booking.patient,
            "Emergency case registered. You are prioritized."
        )

        return queue

    @staticmethod
    def recalculate_hospital_load(hospital):

        from apps.analytics.services import AnalyticsService

        return AnalyticsService.generate_hospital_analytics(hospital)