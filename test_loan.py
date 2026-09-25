"""Tests for Loan dataclass and DateTime / TimeDelta handling."""
from dataclasses import is_dataclass
from datetime import datetime, timedelta

import pytest

from book import Book
from exceptions import InvalidDurationError
from loan import Loan


@pytest.fixture
def sample_book():
    """Returns a sample book for testing."""
    return Book("Clean Code", "Robert C. Martin", "978-0132350884")


def test_loan_is_dataclass():
    """Tests that Loan is implemented as a dataclass."""
    assert is_dataclass(Loan), "Loan must be a @dataclass"


def test_loan_defaults(sample_book):
    """Tests default values for loan."""
    before = datetime.now()
    loan = Loan(book=sample_book)
    after = datetime.now()

    assert loan.book == sample_book
    assert isinstance(loan.duration, timedelta)
    assert loan.duration == timedelta(days=14)
    assert isinstance(loan.borrow_date, datetime)
    assert before <= loan.borrow_date <= after


def test_loan_with_string_date(sample_book):
    """Tests parsing borrow_date from string '%d.%m.%Y'."""
    loan = Loan(book=sample_book, borrow_date="15.10.2026", duration=7)
    assert loan.borrow_date == datetime(2026, 10, 15)
    assert loan.duration == timedelta(days=7)


def test_loan_with_datetime(sample_book):
    """Tests initializing loan with explicit datetime object."""
    dt = datetime(2026, 5, 20, 10, 30)
    loan = Loan(book=sample_book, borrow_date=dt, duration=timedelta(days=21))
    assert loan.borrow_date == dt
    assert loan.duration == timedelta(days=21)


def test_due_date_calculation(sample_book):
    """Tests calculating due_date as borrow_date + duration."""
    loan = Loan(book=sample_book, borrow_date="01.06.2026", duration=14)
    expected_due = datetime(2026, 6, 15)
    assert loan.due_date == expected_due


def test_is_overdue(sample_book):
    """Tests is_overdue method with simulated check dates."""
    loan = Loan(book=sample_book, borrow_date="01.06.2026", duration=14)
    # Due date is 15.06.2026 00:00:00

    # Before due date
    assert not loan.is_overdue(datetime(2026, 6, 10))

    # Exactly on due date
    assert not loan.is_overdue(datetime(2026, 6, 15))

    # After due date
    assert loan.is_overdue(datetime(2026, 6, 16))


def test_invalid_duration_zero_or_negative(sample_book):
    """Tests that duration <= 0 raises InvalidDurationError."""
    with pytest.raises(InvalidDurationError):
        Loan(book=sample_book, duration=0)

    with pytest.raises(InvalidDurationError):
        Loan(book=sample_book, duration=-5)

    with pytest.raises(InvalidDurationError):
        Loan(book=sample_book, duration=timedelta(days=0))


def test_invalid_duration_exceeding_max(sample_book):
    """Tests that duration > 60 days raises InvalidDurationError."""
    with pytest.raises(InvalidDurationError):
        Loan(book=sample_book, duration=61)

    with pytest.raises(InvalidDurationError):
        Loan(book=sample_book, duration=timedelta(days=90))


def test_setters(sample_book):
    """Tests property setters for borrow_date and duration."""
    loan = Loan(book=sample_book, borrow_date="01.01.2026", duration=10)

    loan.borrow_date = "10.02.2026"
    assert loan.borrow_date == datetime(2026, 2, 10)

    loan.duration = 20
    assert loan.duration == timedelta(days=20)
    assert loan.due_date == datetime(2026, 3, 2)
