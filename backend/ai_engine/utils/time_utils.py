from datetime import datetime, UTC


class TimeUtils:

    @staticmethod
    def now():

        return datetime.now(UTC)