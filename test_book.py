"""Tests for Book dataclass."""
from dataclasses import is_dataclass

import pytest

from book import Book


def test_book_is_dataclass():
    """Tests that Book is implemented as a dataclass."""
    assert is_dataclass(Book), "Book must be a @dataclass"


def test_book_attributes():
    """Tests Book attribute initialization and reading."""
    book = Book(title="1984", author="George Orwell", isbn="978-0451524935")
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.isbn == "978-0451524935"


def test_book_equality():
    """Tests dataclass generated equality comparison."""
    book1 = Book("Der Prozess", "Franz Kafka", "978-3150090886")
    book2 = Book("Der Prozess", "Franz Kafka", "978-3150090886")
    assert book1 == book2
