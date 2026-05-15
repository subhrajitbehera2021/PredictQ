from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class RealtimeEventProcessor:

    def __init__(
        self,
        realtime_sync_manager,
        event_dispatcher
    ):

        self.realtime_sync_manager = (
            realtime_sync_manager
        )

        self.event_dispatcher = (
            event_dispatcher
        )

    # =====================================================
    # PROCESS QUEUE UPDATE
    # =====================================================

    def process_queue_update(
        self,
        department: str,
        queue: list
    ):

        logger.info(
            f"Processing realtime queue update "
            f"for {department}"
        )

        # SYNC REALTIME STATE
        self.realtime_sync_manager.sync_department_queue(
            department,
            queue
        )

        # DISPATCH EVENT
        self.event_dispatcher.dispatch(
            "REALTIME_QUEUE_UPDATED",
            {
                "department": department,
                "queue_size": len(queue)
            }
        )

        return {
            "success": True,
            "department": department,
            "queue_size": len(queue)
        }

    # =====================================================
    # PROCESS PATIENT CALL
    # =====================================================

    def process_patient_called(
        self,
        department: str,
        patient: dict
    ):

        logger.info(
            f"Processing patient call event "
            f"{patient.get('patient_id')}"
        )

        self.event_dispatcher.dispatch(
            "REALTIME_PATIENT_CALLED",
            patient
        )

        return {
            "success": True,
            "patient": patient,
            "department": department
        }

    # =====================================================
    # PROCESS DOCTOR STATUS
    # =====================================================

    def process_doctor_status(
        self,
        doctor_data: dict
    ):

        logger.info(
            f"Processing doctor status update "
            f"{doctor_data.get('doctor_id')}"
        )

        self.event_dispatcher.dispatch(
            "REALTIME_DOCTOR_STATUS",
            doctor_data
        )

        return {
            "success": True,
            "doctor": doctor_data
        }

    # =====================================================
    # PROCESS SYSTEM ALERT
    # =====================================================

    def process_system_alert(
        self,
        alert_type: str,
        message: str
    ):

        payload = {
            "alert_type": alert_type,
            "message": message
        }

        logger.warning(
            f"SYSTEM ALERT: {message}"
        )

        self.event_dispatcher.dispatch(
            "REALTIME_SYSTEM_ALERT",
            payload
        )

        return payload