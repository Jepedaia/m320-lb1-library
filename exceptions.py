"""Hier sind custom exceptions abgelegt für die Bibliothek"""

class LibraryError(Exception):
    def __init__(self):
        super().__init__()


class LoanLimitExceededError(LibraryError):
    pass


class InvalidDurationError(LibraryError):
    pass
