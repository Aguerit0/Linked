"""Custom exceptions for the application."""


class AppException(Exception):
    """Base exception for the application."""

    def __init__(self, message: str, status_code: int = 400, detail: str = None):
        self.message = message
        self.status_code = status_code
        self.detail = detail or message
        super().__init__(self.message)


class AuthenticationException(AppException):
    """Raised when authentication fails."""

    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, status_code=401)


class AuthorizationException(AppException):
    """Raised when user doesn't have permission."""

    def __init__(self, message: str = "Not authorized"):
        super().__init__(message, status_code=403)


class NotFoundException(AppException):
    """Raised when resource is not found."""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)


class ConflictException(AppException):
    """Raised when there's a conflict (e.g., duplicate resource)."""

    def __init__(self, message: str = "Resource already exists"):
        super().__init__(message, status_code=409)


class ValidationException(AppException):
    """Raised when validation fails."""

    def __init__(self, message: str = "Validation error"):
        super().__init__(message, status_code=422)
