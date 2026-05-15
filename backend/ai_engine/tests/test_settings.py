from ai_engine.settings import (
    settings
)


def test_engine_info():

    info = settings.get_engine_info()

    assert (
        info["name"]
        == "PredictQ AI Engine"
    )

    assert (
        info["version"]
        == "1.0.0"
    )


def test_environment_helpers():

    assert (
        settings.is_development()
        is True
    )


def test_database_url():

    assert (
        settings.DATABASE_URL
        == "memory://local"
    )