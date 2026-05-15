from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class PredictiveAnalyticsEngine:

    def __init__(self):

        self.prediction_history = []

    # =====================================================
    # PREDICT OVERLOAD RISK
    # =====================================================

    def predict_overload_risk(
        self,
        predicted_load: int,
        available_doctors: int
    ):

        if available_doctors <= 0:
            available_doctors = 1

        load_ratio = (
            predicted_load
            / available_doctors
        )

        if load_ratio >= 30:

            risk = "CRITICAL"

        elif load_ratio >= 15:

            risk = "HIGH"

        elif load_ratio >= 8:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        logger.info(
            f"Overload risk predicted: "
            f"{risk}"
        )

        return risk

    # =====================================================
    # STAFFING RISK
    # =====================================================

    def predict_staffing_risk(
        self,
        predicted_load: int,
        available_doctors: int
    ):

        recommended_doctors = max(
            1,
            round(predicted_load / 10)
        )

        shortage = (
            recommended_doctors
            - available_doctors
        )

        if shortage <= 0:

            status = "SUFFICIENT"

        else:

            status = "SHORTAGE"

        logger.info(
            f"Staffing risk status: "
            f"{status}"
        )

        return {

            "status": status,

            "required_doctors":
            recommended_doctors,

            "doctor_shortage":
            max(shortage, 0)
        }

    # =====================================================
    # QUEUE GROWTH PREDICTION
    # =====================================================

    def predict_queue_growth(
        self,
        current_queue: int,
        predicted_load: int
    ):

        growth = (
            predicted_load
            - current_queue
        )

        logger.info(
            f"Queue growth predicted: "
            f"{growth}"
        )

        return growth

    # =====================================================
    # GENERATE AI RECOMMENDATIONS
    # =====================================================

    def generate_ai_recommendations(
        self,
        overload_risk: str,
        staffing_report: dict
    ):

        recommendations = []

        if overload_risk in [
            "HIGH",
            "CRITICAL"
        ]:

            recommendations.append(
                "Increase doctor allocation immediately"
            )

        if (
            staffing_report["status"]
            == "SHORTAGE"
        ):

            recommendations.append(
                "Schedule additional OPD staff"
            )

        if not recommendations:

            recommendations.append(
                "Hospital operations stable"
            )

        logger.info(
            "AI recommendations generated"
        )

        return recommendations

    # =====================================================
    # COMPLETE PREDICTIVE REPORT
    # =====================================================

    def generate_predictive_report(
        self,
        current_queue: int,
        predicted_load: int,
        available_doctors: int
    ):

        overload_risk = (
            self.predict_overload_risk(
                predicted_load,
                available_doctors
            )
        )

        staffing_report = (
            self.predict_staffing_risk(
                predicted_load,
                available_doctors
            )
        )

        queue_growth = (
            self.predict_queue_growth(
                current_queue,
                predicted_load
            )
        )

        recommendations = (
            self.generate_ai_recommendations(
                overload_risk,
                staffing_report
            )
        )

        report = {

            "overload_risk":
            overload_risk,

            "staffing":
            staffing_report,

            "queue_growth":
            queue_growth,

            "recommendations":
            recommendations
        }

        self.prediction_history.append(
            report
        )

        logger.info(
            "Predictive analytics report generated"
        )

        return report

    # =====================================================
    # GET PREDICTION HISTORY
    # =====================================================

    def get_prediction_history(self):

        return self.prediction_history