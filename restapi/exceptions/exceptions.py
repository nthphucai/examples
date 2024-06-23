class ApiError(Exception):
    """base exception class"""

    def __init__(self, message: str = "Service is unavailable", name: str = "SkyPulse"):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)


class ServiceError(ApiError):
    """failures in external services or APIs, like a database or a third-party service"""

    pass


class TypingError(ApiError):
    """invalid typing input"""

    pass


class UnExpectedError(ApiError):
    """unexpected error"""

    pass
