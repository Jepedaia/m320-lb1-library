"""Library module representing the library managing members and book loans."""
from book import Book
from exceptions import LoanLimitExceededError
from loan import Loan
from member import Member


class Library:
    """Represents a library managing a collection of members.

    Establishes a 1:n bidirectional relationship with Member outside the constructor.
    """

    def __init__(self, name: str):
        """Initializes library with name and empty members list."""
        # TODO: Initialize self._name and self._members list
        raise NotImplementedError("Library.__init__ not implemented yet.")

    def add_member(self, member: Member):
        """Adds a member and sets bidirectional relationship member.library = self.

        Raises:
            OverflowError: If library capacity (50 members) is reached.
        """
        # TODO: Check limit, append member if not present, set member.library = self
        raise NotImplementedError("Library.add_member not implemented yet.")

    def take_member(self, index: int) -> Member:
        """Retrieves member by index.

        Raises:
            IndexError: If index is invalid.
        """
        # TODO: Return member at index or raise IndexError
        raise NotImplementedError("Library.take_member not implemented yet.")

    def count_members(self) -> int:
        """Returns number of registered members."""
        # TODO: Return length of self._members
        raise NotImplementedError("Library.count_members not implemented yet.")

    def show_member_list(self) -> str:
        """Returns string containing all member names separated by newline."""
        # TODO: Return newline-separated string of member names
        raise NotImplementedError("Library.show_member_list not implemented yet.")

    def borrow_book(self, member: Member, book: Book, days: int = 14) -> bool:
        """Attempts to create a loan and add it to the member's card.

        Catches LoanLimitExceededError gracefully and prints error message.

        :param member: The member borrowing the book.
        :param book: The book being borrowed.
        :param days: Duration of the loan in days.
        :return: True if borrow succeeded, False if LoanLimitExceededError was caught.
        """
        # TODO: Try creating a Loan and adding it to member.card.
        # TODO: Catch LoanLimitExceededError, print error message, and return False.
        raise NotImplementedError("Library.borrow_book not implemented yet.")

    def find_member(self, name: str) -> Member | None:
        """Finds and returns member by name, or None if not found."""
        # TODO: Search member by name in self._members
        raise NotImplementedError("Library.find_member not implemented yet.")

    @property
    def name(self) -> str:
        """Returns library name."""
        # TODO: Return internal name
        raise NotImplementedError("Library.name getter not implemented yet.")
