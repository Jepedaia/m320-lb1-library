"""Book module representing a library book item."""
from dataclasses import dataclass


@dataclass
class Book:
    """Represents a book in the library.

    Attributes:
        title (str): Title of the book.
        author (str): Author of the book.
        isbn (str): ISBN identifier of the book.
    """
    # TODO: Define title (str), author (str), and isbn (str) as dataclass fields
    title: str = ""
    author: str = ""
    isbn: str = ""
