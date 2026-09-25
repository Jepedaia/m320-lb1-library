"""Loan module representing a book loan."""
from dataclasses import dataclass
from datetime import datetime, timedelta

from book import Book
from exceptions import InvalidDurationError


@dataclass
class Loan:
    """Represents a book loan with borrow date and duration.

    Attributes:
        book (Book): The borrowed book.
        borrow_date (datetime | str | None): The date when the book was borrowed.
        duration (timedelta | int): The loan duration in days or as timedelta.
    """
    book: Book
    borrow_date: datetime | str | None = None
    duration: timedelta | int = 14

    def __post_init__(self):
        """Initializes internal attributes using properties."""
        # TODO: Initialize and validate properties (e.g. self.borrow_date, self.duration)
        raise NotImplementedError("Loan.__post_init__ not implemented yet.")

    @property
    def book(self) -> Book:
        """Returns the borrowed book."""
        # TODO: Return internal book attribute
        raise NotImplementedError("Loan.book getter not implemented yet.")

    @book.setter
    def book(self, value: Book):
        """Sets the borrowed book."""
        # TODO: Set internal book attribute
        raise NotImplementedError("Loan.book setter not implemented yet.")

    @property
    def borrow_date(self) -> datetime:
        """Returns the borrow date as datetime."""
        # TODO: Return internal borrow_date attribute
        raise NotImplementedError("Loan.borrow_date getter not implemented yet.")

    @borrow_date.setter
    def borrow_date(self, value: datetime | str | None):
        """Sets borrow date. Converts string '%d.%m.%Y' to datetime or defaults to now."""
        # TODO: Validate and convert value to datetime
        raise NotImplementedError("Loan.borrow_date setter not implemented yet.")

    @property
    def duration(self) -> timedelta:
        """Returns the duration as timedelta."""
        # TODO: Return internal duration attribute
        raise NotImplementedError("Loan.duration getter not implemented yet.")

    @duration.setter
    def duration(self, value: timedelta | int):
        """Sets duration. Converts int to timedelta(days=value).

        Raises:
            InvalidDurationError: If duration is <= 0 or > 60 days.
        """
        # TODO: Validate duration (1..60 days) and raise InvalidDurationError if invalid
        raise NotImplementedError("Loan.duration setter not implemented yet.")

    @property
    def due_date(self) -> datetime:
        """Calculates and returns due date (borrow_date + duration)."""
        # TODO: Return borrow_date + duration
        raise NotImplementedError("Loan.due_date getter not implemented yet.")

    def is_overdue(self, check_date: datetime | None = None) -> bool:
        """Checks if the loan is overdue relative to check_date (default now).

        :param check_date: The date to check against (default datetime.now()).
        :return: True if overdue, False otherwise.
        """
        # TODO: Check if check_date > due_date
        raise NotImplementedError("Loan.is_overdue not implemented yet.")
