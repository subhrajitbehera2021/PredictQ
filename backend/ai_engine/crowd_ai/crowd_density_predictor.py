from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class CrowdDensityPredictor:

    def __init__(self):

        self.history = []

    # =====================================================
    # PREDICT CROWD DENSITY
    # =====================================================

    def predict_density(
        self,
        patient_count: int,
        waiting_area_capacity: int
    ):

        if waiting_area_capacity <= 0:
            density = 100
        else:
            density = (
                patient_count
                / waiting_area_capacity
            ) * 100

        density = round(density, 2)

        # CROWD LEVEL
        if density >= 90:

            crowd_level = "CRITICAL"

        elif density >= 70:

            crowd_level = "HIGH"

        elif density >= 40:

            crowd_level = "MEDIUM"

        else:

            crowd_level = "LOW"

        prediction = {

            "patient_count":
            patient_count,

            "waiting_area_capacity":
            waiting_area_capacity,

            "density_percentage":
            density,

            "crowd_level":
            crowd_level
        }

        self.history.append(
            prediction
        )

        logger.info(
            f"Crowd density predicted: "
            f"{crowd_level}"
        )

        return prediction

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
            "Crowd density history reset"
        )