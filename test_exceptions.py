"""Tests for custom exception classes."""
import pytest

from exceptions import InvalidDurationError, LibraryError, LoanLimitExceededError


def test_exception_inheritance():
    """Tests that custom exceptions inherit from LibraryError and Exception."""
    assert issubclass(LibraryError, Exception)
    assert issubclass(LoanLimitExceededError, LibraryError)
    assert issubclass(InvalidDurationError, LibraryError)


def test_raise_loan_limit_exceeded_error():
    """Tests raising and catching LoanLimitExceededError."""
    with pytest.raises(LoanLimitExceededError) as exc_info:
        raise LoanLimitExceededError("Ausleihlimit erreicht")
    assert "Ausleihlimit erreicht" in str(exc_info.value)


def test_raise_invalid_duration_error():
    """Tests raising and catching InvalidDurationError."""
    with pytest.raises(InvalidDurationError) as exc_info:
        raise InvalidDurationError("Dauer ungueltig")
    assert "Dauer ungueltig" in str(exc_info.value)
