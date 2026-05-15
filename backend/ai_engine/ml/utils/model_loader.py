import os
import pickle

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class ModelLoader:

    def __init__(self):

        self.loaded_models = []

    # =====================================================
    # LOAD MODEL
    # =====================================================

    def load_model(
        self,
        model_path: str
    ):

        if not os.path.exists(
            model_path
        ):

            raise FileNotFoundError(
                f"Model not found: "
                f"{model_path}"
            )

        with open(
            model_path,
            "rb"
        ) as file:

            model = pickle.load(file)

        self.loaded_models.append(
            model_path
        )

        logger.info(
            f"Model loaded: "
            f"{model_path}"
        )

        return model

    # =====================================================
    # GET LOADED MODELS
    # =====================================================

    def get_loaded_models(self):

        return self.loaded_models