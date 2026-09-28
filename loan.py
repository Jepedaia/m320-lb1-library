from dataclasses import dataclass
from datetime import datetime, timedelta

from book import Book
from exceptions import InvalidDurationError


@dataclass
class Loan:
    book: Book
    borrow_date: datetime | str | None = None
    duration: timedelta | int = 14

    def __post_init__(self):
        # TODO: Initialize and validate properties (e.g. self.borrow_date, self.duration)
        raise NotImplementedError("Loan.__post_init__ not implemented yet.")

    @property
    def book(self) -> Book:
        # TODO: Return book
        raise NotImplementedError("Loan.book getter not implemented yet.")

    @book.setter
    def book(self, value: Book):
        # TODO: Set book
        raise NotImplementedError("Loan.book setter not implemented yet.")

    @property
    def borrow_date(self) -> datetime:
        # TODO: Return borrow_date
        raise NotImplementedError("Loan.borrow_date getter not implemented yet.")

    @borrow_date.setter
    def borrow_date(self, value: datetime | str | None):
        # TODO: Validate and convert value to datetime
        raise NotImplementedError("Loan.borrow_date setter not implemented yet.")

    @property
    def duration(self) -> timedelta:
        # TODO: Return duration
        raise NotImplementedError("Loan.duration getter not implemented yet.")

    @duration.setter
    def duration(self, value: timedelta | int):
        # TODO: Validate duration (1..60 days) and raise InvalidDurationError if invalid
        raise NotImplementedError("Loan.duration setter not implemented yet.")

    @property
    def due_date(self) -> datetime:
        # TODO: Return borrow_date + duration
        raise NotImplementedError("Loan.due_date getter not implemented yet.")

    def is_overdue(self, check_date: datetime | None = None) -> bool:
        # TODO: Check if check_date > due_date
        raise NotImplementedError("Loan.is_overdue not implemented yet.")
