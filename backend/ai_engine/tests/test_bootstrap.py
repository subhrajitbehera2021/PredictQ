from ai_engine.bootstrap import (
    EngineBootstrap,
    engine
)


def test_configuration_loading():

    bootstrap = EngineBootstrap()

    result = bootstrap.load_configuration()

    assert result["name"] == "PredictQ AI Engine"


def test_runtime_start():

    bootstrap = EngineBootstrap()

    result = bootstrap.start_runtime()

    assert result is True


def test_default_departments():

    bootstrap = EngineBootstrap()

    result = bootstrap.create_default_departments()

    assert "cardiology" in result
    assert "neurology" in result


def test_listener_registration():

    bootstrap = EngineBootstrap()

    result = bootstrap.register_listeners()

    assert result is True


def test_model_loading():

    bootstrap = EngineBootstrap()

    result = bootstrap.load_models()

    assert result["eta_model"] == "loaded"


def test_health_check():

    bootstrap = EngineBootstrap()

    result = bootstrap.run_health_check()

    assert result["engine"] == "healthy"


def test_initialize():

    bootstrap = EngineBootstrap()

    result = bootstrap.initialize()

    assert result["boot_status"]["initialized"] is True


def test_global_engine_exists():

    assert engine is not None