from ai_engine.security_ai.access_control_manager import (
    AccessControlManager
)


manager = AccessControlManager()


def test_role_validation():

    assert (
        manager.validate_role(
            "ADMIN"
        )
        is True
    )


def test_permission_check():

    assert (
        manager.has_permission(
            "ADMIN",
            "VIEW_ANALYTICS"
        )
        is True
    )


def test_register_role():

    result = manager.register_role(
        "SUPERVISOR",
        ["VIEW_REPORTS"]
    )

    assert (
        result["role"]
        == "SUPERVISOR"
    )