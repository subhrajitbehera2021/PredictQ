from rest_framework.response import Response


class SuccessResponse(Response):

    def __init__(
        self,
        data=None,
        message="Success",
        status=200
    ):

        response = {
            "success": True,
            "message": message,
            "data": data,
        }

        super().__init__(response, status=status)


class ErrorResponse(Response):

    def __init__(
        self,
        message="Error",
        errors=None,
        status=400
    ):

        response = {
            "success": False,
            "message": message,
            "errors": errors,
        }

        super().__init__(response, status=status)