from api.security.jwt_handler import (
    JWTHandler
)


def test_create_access_token():

    token = JWTHandler.create_access_token(
        {
            "user_id": "U001",
            "role": "ADMIN"
        }
    )

    assert isinstance(token, str)


def test_verify_valid_token():

    token = JWTHandler.create_user_token(
        user_id="U001",
        role="ADMIN"
    )

    result = JWTHandler.verify_token(
        token
    )

    assert result["valid"] is True
    assert result["payload"]["user_id"] == "U001"
    assert result["payload"]["role"] == "ADMIN"


def test_verify_invalid_token():

    result = JWTHandler.verify_token(
        "invalid.token.value"
    )

    assert result["valid"] is False