from ai_engine.ml.inference.eta_inference import (
    ETAInference
)

from ai_engine.ml.inference.no_show_inference import (
    NoShowInference
)

from ai_engine.ml.inference.crowd_inference import (
    CrowdInference
)

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class InferencePipeline:

    def __init__(self):

        self.eta_inference = ETAInference()

        self.no_show_inference = (
            NoShowInference()
        )

        self.crowd_inference = (
            CrowdInference()
        )

        self.pipeline_history = []

    # =====================================================
    # RUN COMPLETE PIPELINE
    # =====================================================

    def run_pipeline(
        self,
        payload: dict
    ):

        eta_result = (
            self.eta_inference.predict_eta(
                payload.get(
                    "eta_features",
                    {}
                )
            )
        )

        no_show_result = (
            self.no_show_inference.predict_no_show(
                payload.get(
                    "no_show_features",
                    {}
                )
            )
        )

        crowd_result = (
            self.crowd_inference.predict_crowd(
                payload.get(
                    "crowd_features",
                    {}
                )
            )
        )

        result = {

            "eta_prediction":
            eta_result,

            "no_show_prediction":
            no_show_result,

            "crowd_prediction":
            crowd_result
        }

        self.pipeline_history.append(
            result
        )

        logger.info(
            "Inference pipeline executed"
        )

        return result

    # =====================================================
    # GET PIPELINE HISTORY
    # =====================================================

    def get_pipeline_history(self):

        return self.pipeline_history

    # =====================================================
    # CLEAR PIPELINE HISTORY
    # =====================================================

    def clear_history(self):

        self.pipeline_history = []

        logger.info(
            "Inference pipeline history cleared"
        )