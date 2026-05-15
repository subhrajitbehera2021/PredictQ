from ai_engine.audit_ai.audit_logger import (
    AuditLogger
)


logger = AuditLogger()


def test_patient_registration_audit():

    result = (
        logger.log_patient_registration(
            patient_id="P001",
            department="cardiology"
        )
    )

    assert (
        result["event_type"]
        == "PATIENT_REGISTERED"
    )


def test_security_event():

    result = (
        logger.log_security_event(
            "FAILED_LOGIN",
            "admin"
        )
    )

    assert (
        result["event_type"]
        == "SECURITY_EVENT"
    )


def test_ai_decision_audit():

    result = (
        logger.log_ai_decision(
            "REALLOCATE_DOCTOR",
            {
                "from": "neurology",
                "to": "cardiology"
            }
        )
    )

    assert (
        result["actor"]
        == "AI_ENGINE"
    )