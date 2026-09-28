from datetime import datetime

from exceptions import LoanLimitExceededError
from loan import Loan


class LibraryCard:

    def __init__(self, member=None):
        # TODO: Initialize loans list and member (encapsulated according to coding standards)
        raise NotImplementedError("LibraryCard.__init__ not implemented yet.")

    def add_loan(self, loan: Loan):
        # TODO: Check limit (max 5) and add loan if not already present
        raise NotImplementedError("LibraryCard.add_loan not implemented yet.")

    def take_loan(self, index: int) -> Loan:
        # TODO: Return loan at index or raise IndexError
        raise NotImplementedError("LibraryCard.take_loan not implemented yet.")

    def count_loans(self) -> int:
        # TODO: Return number of loans
        raise NotImplementedError("LibraryCard.count_loans not implemented yet.")

    def count_overdue_loans(self, current_date: datetime | None = None) -> int:
        # TODO: Count overdue loans using loan.is_overdue(current_date)
        raise NotImplementedError("LibraryCard.count_overdue_loans not implemented yet.")

    def show_overview(self) -> str:
        # TODO: Return string like 'Card for <member_name>: <count> loans'
        raise NotImplementedError("LibraryCard.show_overview not implemented yet.")

    @property
    def member(self):
        # TODO: Return member
        raise NotImplementedError("LibraryCard.member getter not implemented yet.")

    @member.setter
    def member(self, value):
        # TODO: Set member
        raise NotImplementedError("LibraryCard.member setter not implemented yet.")
