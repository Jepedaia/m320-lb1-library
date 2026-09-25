"""Tests for Library class, 1:n bidirectional relationship, and exception handling."""
import pytest

from book import Book
from library import Library
from library_card import LibraryCard
from member import Member


@pytest.fixture
def library():
    """Returns a Library fixture."""
    return Library("Stadtbibliothek BZZ")


@pytest.fixture
def members():
    """Returns a list of two distinct members with cards."""
    return [
        Member("Anna Meier", LibraryCard()),
        Member("Ben Keller", LibraryCard()),
    ]


@pytest.fixture
def book():
    """Returns a sample book."""
    return Book("Clean Code", "Robert C. Martin", "978-0132350884")


def test_library_initialisation(library):
    """Tests Library constructor sets name and initializes empty members."""
    assert library.name == "Stadtbibliothek BZZ"
    assert library.count_members() == 0


def test_add_member_bidirectional_relationship(library, members):
    """Tests adding a member establishes 1:n relationship outside constructor."""
    anna = members[0]
    library.add_member(anna)

    assert library.count_members() == 1
    assert anna.library is library
    assert library.take_member(0) is anna


def test_add_duplicate_member_ignored(library, members):
    """Tests adding the same member twice does not duplicate."""
    anna = members[0]
    library.add_member(anna)
    library.add_member(anna)
    assert library.count_members() == 1


def test_take_member_invalid_index(library):
    """Tests take_member with invalid index raises IndexError."""
    with pytest.raises(IndexError):
        library.take_member(0)


def test_show_member_list(library, members):
    """Tests show_member_list contains added member names."""
    library.add_member(members[0])
    library.add_member(members[1])

    member_list = library.show_member_list()
    assert "Anna Meier" in member_list
    assert "Ben Keller" in member_list


def test_find_member(library, members):
    """Tests finding member by name."""
    library.add_member(members[0])
    assert library.find_member("Anna Meier") is members[0]
    assert library.find_member("Unbekannt") is None


def test_borrow_book_success(library, members, book):
    """Tests successful borrow_book returns True and updates card."""
    anna = members[0]
    library.add_member(anna)

    result = library.borrow_book(anna, book, days=14)
    assert result is True
    assert anna.card.count_loans() == 1
    assert anna.card.take_loan(0).book == book


def test_borrow_book_catches_loan_limit_exceeded_error(library, members, capsys):
    """Tests that borrow_book catches LoanLimitExceededError and returns False."""
    anna = members[0]
    library.add_member(anna)

    # Add 5 books to reach limit
    for i in range(5):
        b = Book(f"Title {i}", f"Author {i}", f"ISBN-{i}")
        assert library.borrow_book(anna, b, days=14) is True

    assert anna.card.count_loans() == 5

    # 6th book should be caught gracefully without crashing
    extra_book = Book("Extra Book", "Extra Author", "ISBN-999")
    result = library.borrow_book(anna, extra_book, days=7)

    assert result is False
    assert anna.card.count_loans() == 5

    # Verify that an error message was printed to console
    captured = capsys.readouterr()
    assert "Anna Meier" in captured.out or "Ausleihlimit" in captured.out or "Limit" in captured.out
