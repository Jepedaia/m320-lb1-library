"""LibraryCard module representing a member's library card and active loans."""
from datetime import datetime

from exceptions import LoanLimitExceededError
from loan import Loan


class LibraryCard:
    """Represents a library card holding a list of loans.

    Max capacity: 5 loans.
    """

    def __init__(self, member=None):
        """Initializes empty loans list and sets optional member reference."""
        # TODO: Initialize self._loans as list and self._member
        raise NotImplementedError("LibraryCard.__init__ not implemented yet.")

    def add_loan(self, loan: Loan):
        """Adds a loan to the card.

        Raises:
            LoanLimitExceededError: If the card already has 5 active loans.
        """
        # TODO: Check limit (max 5) and add loan to self._loans if not already present
        raise NotImplementedError("LibraryCard.add_loan not implemented yet.")

    def take_loan(self, index: int) -> Loan:
        """Retrieves a loan by index.

        Raises:
            IndexError: If index is invalid.
        """
        # TODO: Return loan at index or raise IndexError
        raise NotImplementedError("LibraryCard.take_loan not implemented yet.")

    def count_loans(self) -> int:
        """Returns the number of active loans."""
        # TODO: Return length of self._loans
        raise NotImplementedError("LibraryCard.count_loans not implemented yet.")

    def count_overdue_loans(self, current_date: datetime | None = None) -> int:
        """Returns the number of loans that are overdue relative to current_date."""
        # TODO: Count overdue loans using loan.is_overdue(current_date)
        raise NotImplementedError("LibraryCard.count_overdue_loans not implemented yet.")

    def show_overview(self) -> str:
        """Returns a string overview of the card and loan count."""
        # TODO: Return string like 'Card for <member_name>: <count> loans'
        raise NotImplementedError("LibraryCard.show_overview not implemented yet.")

    @property
    def member(self):
        """Returns the member associated with this card."""
        # TODO: Return internal member attribute
        raise NotImplementedError("LibraryCard.member getter not implemented yet.")

    @member.setter
    def member(self, value):
        """Sets the member associated with this card."""
        # TODO: Set internal member attribute
        raise NotImplementedError("LibraryCard.member setter not implemented yet.")
