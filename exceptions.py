"""Custom exception classes for the Library Management System."""


class LibraryError(Exception):
    """Base exception for all library errors."""


class LoanLimitExceededError(LibraryError):
    """Raised when a member card reaches its maximum loan limit."""


class InvalidDurationError(LibraryError):
    """Raised when a loan duration is invalid (<= 0 or > 60 days)."""
