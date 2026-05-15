from ai_engine.ml.inference.eta_inference import (
    ETAInference
)

from ai_engine.ml.inference.crowd_inference import (
    CrowdInference
)

from ai_engine.ml.inference.no_show_inference import (
    NoShowInference
)

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class RealtimePipeline:

    def __init__(self):

        self.eta_inference = ETAInference()

        self.crowd_inference = (
            CrowdInference()
        )

        self.no_show_inference = (
            NoShowInference()
        )

        self.pipeline_history = []

    # =====================================================
    # PROCESS REALTIME DATA
    # =====================================================

    def process_realtime_data(
        self,
        patient_data: dict
    ):

        eta_prediction = (
            self.eta_inference.predict_eta(
                patient_data
            )
        )

        crowd_prediction = (
            self.crowd_inference.predict_crowd(
                patient_data
            )
        )

        no_show_prediction = (
            self.no_show_inference.predict_no_show(
                patient_data
            )
        )

        result = {

            "eta_prediction":
            eta_prediction,

            "crowd_prediction":
            crowd_prediction,

            "no_show_prediction":
            no_show_prediction
        }

        self.pipeline_history.append(
            result
        )

        logger.info(
            "Realtime pipeline executed"
        )

        return result

    # =====================================================
    # GET PIPELINE HISTORY
    # =====================================================

    def get_pipeline_history(self):

        return self.pipeline_history