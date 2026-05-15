from datetime import datetime, timedelta, UTC

from jose import jwt, JWTError


class JWTHandler:

    SECRET_KEY = "predictq_secret_key_change_in_production"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    @classmethod
    def create_access_token(
        cls,
        data: dict,
        expires_delta: timedelta | None = None
    ):

        payload = data.copy()

        expire = datetime.now(UTC) + (
            expires_delta
            if expires_delta
            else timedelta(
                minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        )

        payload.update(
            {
                "exp": expire
            }
        )

        token = jwt.encode(
            payload,
            cls.SECRET_KEY,
            algorithm=cls.ALGORITHM
        )

        return token

    @classmethod
    def verify_token(
        cls,
        token: str
    ):

        try:

            payload = jwt.decode(
                token,
                cls.SECRET_KEY,
                algorithms=[
                    cls.ALGORITHM
                ]
            )

            return {
                "valid": True,
                "payload": payload
            }

        except JWTError as error:

            return {
                "valid": False,
                "error": str(error)
            }

    @classmethod
    def create_user_token(
        cls,
        user_id: str,
        role: str
    ):

        return cls.create_access_token(
            {
                "user_id": user_id,
                "role": role
            }
        )