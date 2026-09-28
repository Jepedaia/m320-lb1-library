from book import Book
from exceptions import LoanLimitExceededError
from loan import Loan
from member import Member


class Library:

    def __init__(self, name: str):
        # TODO: Initialize name and members list
        raise NotImplementedError("Library.__init__ not implemented yet.")

    def add_member(self, member: Member):
        # TODO: Check limit, append member if not present, set member.library = self
        raise NotImplementedError("Library.add_member not implemented yet.")

    def take_member(self, index: int) -> Member:
        # TODO: Return member at index or raise IndexError
        raise NotImplementedError("Library.take_member not implemented yet.")

    def count_members(self) -> int:
        # TODO: Return count of members
        raise NotImplementedError("Library.count_members not implemented yet.")

    def show_member_list(self) -> str:
        # TODO: Return newline-separated string of member names
        raise NotImplementedError("Library.show_member_list not implemented yet.")

    def borrow_book(self, member: Member, book: Book, days: int = 14) -> bool:
        # TODO: Try creating a Loan and adding it to member.card.
        # TODO: Catch LoanLimitExceededError, print error message, and return False.
        raise NotImplementedError("Library.borrow_book not implemented yet.")

    def find_member(self, name: str) -> Member | None:
        # TODO: Search member by name in members
        raise NotImplementedError("Library.find_member not implemented yet.")

    @property
    def name(self) -> str:
        # TODO: Return name
        raise NotImplementedError("Library.name getter not implemented yet.")
