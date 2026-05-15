from ai_engine.registry import (
    EngineRegistry,
    registry
)


def test_register_component():

    local_registry = (
        EngineRegistry()
    )

    result = (
        local_registry.register(
            "test_component",
            object()
        )
    )

    assert result is True


def test_get_component():

    local_registry = (
        EngineRegistry()
    )

    component = object()

    local_registry.register(
        "sample",
        component
    )

    assert (
        local_registry.get(
            "sample"
        )
        == component
    )


def test_remove_component():

    local_registry = (
        EngineRegistry()
    )

    local_registry.register(
        "temp",
        object()
    )

    result = (
        local_registry.remove(
            "temp"
        )
    )

    assert result is True


def test_list_components():

    local_registry = (
        EngineRegistry()
    )

    local_registry.register(
        "a",
        object()
    )

    local_registry.register(
        "b",
        object()
    )

    components = (
        local_registry.list_components()
    )

    assert "a" in components
    assert "b" in components


def test_clear_registry():

    local_registry = (
        EngineRegistry()
    )

    local_registry.register(
        "x",
        object()
    )

    local_registry.clear()

    assert (
        local_registry.size()
        == 0
    )


def test_global_registry():

    components = (
        registry.list_components()
    )

    assert "engine" in components
    assert "settings" in components
    assert "bootstrap" in components