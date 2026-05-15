import os
import pickle

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class ModelSaver:

    def __init__(self):

        self.saved_models = []

    # =====================================================
    # SAVE MODEL
    # =====================================================

    def save_model(
        self,
        model,
        model_name: str,
        directory: str
    ):

        os.makedirs(
            directory,
            exist_ok=True
        )

        model_path = os.path.join(
            directory,
            f"{model_name}.pkl"
        )

        with open(
            model_path,
            "wb"
        ) as file:

            pickle.dump(
                model,
                file
            )

        self.saved_models.append(
            model_path
        )

        logger.info(
            f"Model saved: {model_path}"
        )

        return model_path

    # =====================================================
    # GET SAVED MODELS
    # =====================================================

    def get_saved_models(self):

        return self.saved_models