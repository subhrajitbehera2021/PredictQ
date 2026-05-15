from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class ConsultationTimePredictor:

    def __init__(self):

        self.history = []

    # =====================================================
    # PREDICT CONSULTATION TIME
    # =====================================================

    def predict_time(
        self,
        patient_age: int,
        symptoms_count: int,
        priority: int
    ):

        base_time = 10

        # AGE FACTOR
        if patient_age >= 60:
            base_time += 5

        # SYMPTOM FACTOR
        base_time += (
            symptoms_count * 2
        )

        # PRIORITY FACTOR
        base_time += (
            priority * 3
        )

        predicted_time = round(base_time)

        prediction = {

            "predicted_minutes":
            predicted_time,

            "patient_age":
            patient_age,

            "symptoms_count":
            symptoms_count,

            "priority":
            priority
        }

        self.history.append(
            prediction
        )

        logger.info(
            f"Consultation time predicted: "
            f"{predicted_time} mins"
        )

        return prediction

    # =====================================================
    # AVERAGE CONSULTATION TIME
    # =====================================================

    def average_consultation_time(self):

        if not self.history:
            return 0

        total = sum(
            item["predicted_minutes"]
            for item in self.history
        )

        avg = total / len(self.history)

        return round(avg, 2)

    # =====================================================
    # GET HISTORY
    # =====================================================

    def get_history(self):

        return self.history

    # =====================================================
    # RESET HISTORY
    # =====================================================

    def reset_history(self):

        self.history = []

        logger.info(
            "Consultation prediction history reset"
        )