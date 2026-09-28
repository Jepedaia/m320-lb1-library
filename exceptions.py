class LibraryError(Exception):
    pass


class LoanLimitExceededError(LibraryError):
    pass


class InvalidDurationError(LibraryError):
    pass
