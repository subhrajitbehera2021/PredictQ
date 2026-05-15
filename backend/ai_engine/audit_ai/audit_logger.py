from ai_engine.utils.logging_utils import (
    get_logger
)

from ai_engine.utils.time_utils import (
    TimeUtils
)


logger = get_logger(__name__)


class AuditLogger:

    def __init__(self):

        self.audit_logs = []

    # =====================================================
    # GENERIC AUDIT EVENT
    # =====================================================

    def log_event(
        self,
        event_type: str,
        actor: str,
        details: dict
    ):

        audit_entry = {

            "timestamp":
            str(TimeUtils.now()),

            "event_type":
            event_type,

            "actor":
            actor,

            "details":
            details
        }

        self.audit_logs.append(
            audit_entry
        )

        logger.info(
            f"Audit event logged: "
            f"{event_type}"
        )

        return audit_entry

    # =====================================================
    # PATIENT REGISTRATION AUDIT
    # =====================================================

    def log_patient_registration(
        self,
        patient_id: str,
        department: str,
        actor: str = "SYSTEM"
    ):

        return self.log_event(
            "PATIENT_REGISTERED",
            actor,
            {
                "patient_id": patient_id,
                "department": department
            }
        )

    # =====================================================
    # DOCTOR ASSIGNMENT AUDIT
    # =====================================================

    def log_doctor_assignment(
        self,
        doctor_id: str,
        patient_id: str,
        actor: str = "SYSTEM"
    ):

        return self.log_event(
            "DOCTOR_ASSIGNED",
            actor,
            {
                "doctor_id": doctor_id,
                "patient_id": patient_id
            }
        )

    # =====================================================
    # SECURITY EVENT AUDIT
    # =====================================================

    def log_security_event(
        self,
        event_name: str,
        actor: str
    ):

        return self.log_event(
            "SECURITY_EVENT",
            actor,
            {
                "event_name": event_name
            }
        )

    # =====================================================
    # AI DECISION AUDIT
    # =====================================================

    def log_ai_decision(
        self,
        decision_type: str,
        payload: dict
    ):

        return self.log_event(
            "AI_DECISION",
            "AI_ENGINE",
            {
                "decision_type":
                decision_type,

                "payload":
                payload
            }
        )

    # =====================================================
    # GET AUDIT LOGS
    # =====================================================

    def get_logs(self):

        return self.audit_logs

    # =====================================================
    # CLEAR LOGS
    # =====================================================

    def clear_logs(self):

        self.audit_logs = []

        logger.info(
            "Audit logs cleared"
        )