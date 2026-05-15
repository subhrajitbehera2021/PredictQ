import os

from ai_engine.ml.utils.model_saver import (
    ModelSaver
)

from ai_engine.ml.utils.model_loader import (
    ModelLoader
)


saver = ModelSaver()
loader = ModelLoader()


sample_model = {
    "model": "dummy"
}


def test_save_model():

    path = saver.save_model(
        sample_model,
        "test_model",
        "temp_models"
    )

    assert os.path.exists(path)


def test_load_model():

    path = saver.save_model(
        sample_model,
        "load_test_model",
        "temp_models"
    )

    model = loader.load_model(path)

    assert model["model"] == "dummy"


def test_saved_model_history():

    models = saver.get_saved_models()

    assert len(models) >= 1