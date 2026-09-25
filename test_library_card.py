"""Tests for LibraryCard class."""
from datetime import datetime

import pytest

from book import Book
from exceptions import LoanLimitExceededError
from library_card import LibraryCard
from loan import Loan


@pytest.fixture
def empty_card():
    """Returns an empty library card."""
    return LibraryCard()


@pytest.fixture
def sample_books():
    """Returns a list of 6 distinct books."""
    return [
        Book(f"Title {i}", f"Author {i}", f"ISBN-{i}")
        for i in range(1, 7)
    ]


def test_empty_card(empty_card):
    """Tests initial state of a library card."""
    assert empty_card.count_loans() == 0
    assert empty_card.member is None


def test_add_single_loan(empty_card, sample_books):
    """Tests adding a single loan to the card."""
    loan = Loan(book=sample_books[0])
    empty_card.add_loan(loan)
    assert empty_card.count_loans() == 1


def test_add_multiple_loans(empty_card, sample_books):
    """Tests adding multiple loans up to limit (5)."""
    for i in range(5):
        empty_card.add_loan(Loan(book=sample_books[i]))
    assert empty_card.count_loans() == 5


def test_add_duplicate_loan_ignored(empty_card, sample_books):
    """Tests that re-adding the same loan does not duplicate it."""
    loan = Loan(book=sample_books[0])
    empty_card.add_loan(loan)
    empty_card.add_loan(loan)
    assert empty_card.count_loans() == 1


def test_exceeding_loan_limit_raises_error(empty_card, sample_books):
    """Tests that adding a 6th loan raises LoanLimitExceededError."""
    for i in range(5):
        empty_card.add_loan(Loan(book=sample_books[i]))

    with pytest.raises(LoanLimitExceededError):
        empty_card.add_loan(Loan(book=sample_books[5]))

    assert empty_card.count_loans() == 5


def test_take_loan_valid_index(empty_card, sample_books):
    """Tests retrieving loan by valid index."""
    loan1 = Loan(book=sample_books[0])
    loan2 = Loan(book=sample_books[1])
    empty_card.add_loan(loan1)
    empty_card.add_loan(loan2)

    assert empty_card.take_loan(0) is loan1
    assert empty_card.take_loan(1) is loan2


def test_take_loan_invalid_index(empty_card, sample_books):
    """Tests retrieving loan by invalid index raises IndexError."""
    empty_card.add_loan(Loan(book=sample_books[0]))

    with pytest.raises(IndexError):
        empty_card.take_loan(1)

    with pytest.raises(IndexError):
        empty_card.take_loan(-1)


def test_count_overdue_loans(empty_card, sample_books):
    """Tests counting overdue loans based on a target check date."""
    # Loan 1: borrowed 01.01.2026 for 10 days -> due 11.01.2026
    loan1 = Loan(book=sample_books[0], borrow_date="01.01.2026", duration=10)
    # Loan 2: borrowed 01.01.2026 for 30 days -> due 31.01.2026
    loan2 = Loan(book=sample_books[1], borrow_date="01.01.2026", duration=30)

    empty_card.add_loan(loan1)
    empty_card.add_loan(loan2)

    # Check on 15.01.2026: loan1 is overdue, loan2 is not
    check_date = datetime(2026, 1, 15)
    assert empty_card.count_overdue_loans(check_date) == 1

    # Check on 05.02.2026: both are overdue
    assert empty_card.count_overdue_loans(datetime(2026, 2, 5)) == 2


def test_show_overview(empty_card, sample_books):
    """Tests show_overview output format."""
    empty_card.add_loan(Loan(book=sample_books[0]))
    overview = empty_card.show_overview()
    assert isinstance(overview, str)
    assert "1" in overview
