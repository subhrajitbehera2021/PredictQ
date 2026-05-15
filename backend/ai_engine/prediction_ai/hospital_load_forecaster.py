from statistics import mean

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class HospitalLoadForecaster:

    def __init__(self):

        self.forecast_history = []

    # =====================================================
    # FORECAST PATIENT LOAD
    # =====================================================

    def forecast_patient_load(
        self,
        historical_loads: list
    ):

        if not historical_loads:

            logger.warning(
                "No historical loads provided"
            )

            return 0

        average_load = round(
            mean(historical_loads),
            2
        )

        logger.info(
            f"Forecasted patient load: "
            f"{average_load}"
        )

        self.forecast_history.append(
            average_load
        )

        return average_load

    # =====================================================
    # DETECT PEAK LOAD
    # =====================================================

    def detect_peak_load(
        self,
        predicted_load: float,
        threshold: int = 50
    ):

        peak_detected = (
            predicted_load >= threshold
        )

        logger.info(
            f"Peak load detected: "
            f"{peak_detected}"
        )

        return peak_detected

    # =====================================================
    # STAFF REQUIREMENT ESTIMATION
    # =====================================================

    def estimate_staff_requirements(
        self,
        predicted_load: float,
        patients_per_doctor: int = 10
    ):

        required_doctors = max(
            1,
            round(
                predicted_load
                / patients_per_doctor
            )
        )

        logger.info(
            f"Estimated doctor requirement: "
            f"{required_doctors}"
        )

        return required_doctors

    # =====================================================
    # COMPLETE FORECAST REPORT
    # =====================================================

    def generate_forecast_report(
        self,
        historical_loads: list
    ):

        predicted_load = (
            self.forecast_patient_load(
                historical_loads
            )
        )

        peak_detected = (
            self.detect_peak_load(
                predicted_load
            )
        )

        required_doctors = (
            self.estimate_staff_requirements(
                predicted_load
            )
        )

        report = {

            "predicted_load":
            predicted_load,

            "peak_detected":
            peak_detected,

            "recommended_doctors":
            required_doctors
        }

        logger.info(
            "Forecast report generated"
        )

        return report

    # =====================================================
    # GET FORECAST HISTORY
    # =====================================================

    def get_forecast_history(self):

        return self.forecast_history