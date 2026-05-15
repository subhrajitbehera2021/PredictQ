from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class PatientPriorityEngine:

    def __init__(self):

        self.priority_labels = {
            1: "NORMAL",
            2: "MEDIUM",
            3: "HIGH",
            4: "CRITICAL",
            5: "EMERGENCY"
        }

    # =====================================================
    # CALCULATE PRIORITY SCORE
    # =====================================================

    def calculate_priority(
        self,
        patient_data: dict
    ):

        age = patient_data.get(
            "age",
            30
        )

        emergency = patient_data.get(
            "emergency",
            False
        )

        disability = patient_data.get(
            "disability",
            False
        )

        severity = patient_data.get(
            "severity",
            "normal"
        ).lower()

        vip = patient_data.get(
            "vip",
            False
        )

        score = 1

        # ============================================
        # AGE FACTOR
        # ============================================

        if age >= 65:
            score += 1

        # ============================================
        # DISABILITY FACTOR
        # ============================================

        if disability:
            score += 1

        # ============================================
        # EMERGENCY FACTOR
        # ============================================

        if emergency:
            score += 2

        # ============================================
        # SEVERITY FACTOR
        # ============================================

        severity_scores = {
            "normal": 0,
            "medium": 1,
            "high": 2,
            "critical": 4
        }

        score += severity_scores.get(
            severity,
            0
        )

        # ============================================
        # VIP PRIORITY
        # ============================================

        if vip:
            score += 1

        # ============================================
        # LIMIT SCORE
        # ============================================

        final_score = min(score, 5)

        logger.info(
            f"Priority calculated for "
            f"{patient_data.get('patient_id')} "
            f"| Score: {final_score}"
        )

        return final_score

    # =====================================================
    # GET PRIORITY LABEL
    # =====================================================

    def get_priority_label(
        self,
        priority_score: int
    ):

        return self.priority_labels.get(
            priority_score,
            "UNKNOWN"
        )

    # =====================================================
    # ENRICH PATIENT DATA
    # =====================================================

    def enrich_patient_priority(
        self,
        patient_data: dict
    ):

        priority_score = (
            self.calculate_priority(
                patient_data
            )
        )

        patient_data["priority"] = (
            priority_score
        )

        patient_data["priority_label"] = (
            self.get_priority_label(
                priority_score
            )
        )

        return patient_data