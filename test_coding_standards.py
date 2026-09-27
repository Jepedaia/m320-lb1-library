"""Tests verifying adherence to BZZ coding standards and PEP 8."""
import inspect
import subprocess
import sys

import book
import exceptions
import library
import library_card
import loan
import member
from book import Book
from library import Library
from library_card import LibraryCard
from loan import Loan
from member import Member


def test_data_encapsulation_properties():
    """Verifies that all domain classes strictly encapsulate state using @property."""
    # Member properties
    name_prop = inspect.getattr_static(Member, "name", None)
    assert isinstance(name_prop, property), "Codingstandards-Fehler: 'Member.name' muss als @property gekapselt sein."
    assert name_prop.fset is None, "Codingstandards-Fehler: 'Member.name' darf keinen Setter haben (read-only)."

    card_prop = inspect.getattr_static(Member, "card", None)
    assert isinstance(card_prop, property), "Codingstandards-Fehler: 'Member.card' muss als @property gekapselt sein."
    assert card_prop.fset is None, "Codingstandards-Fehler: 'Member.card' darf keinen Setter haben (read-only)."

    lib_prop = inspect.getattr_static(Member, "library", None)
    assert isinstance(lib_prop, property), "Codingstandards-Fehler: 'Member.library' muss als @property gekapselt sein."
    assert lib_prop.fset is not None, "Codingstandards-Fehler: 'Member.library' muss einen @setter besitzen."

    # Library properties
    lib_name_prop = inspect.getattr_static(Library, "name", None)
    assert isinstance(lib_name_prop, property), "Codingstandards-Fehler: 'Library.name' muss als @property gekapselt sein."
    assert lib_name_prop.fset is None, "Codingstandards-Fehler: 'Library.name' darf keinen Setter haben (read-only)."

    # LibraryCard properties
    card_mem_prop = inspect.getattr_static(LibraryCard, "member", None)
    assert isinstance(card_mem_prop, property), "Codingstandards-Fehler: 'LibraryCard.member' muss als @property gekapselt sein."
    assert card_mem_prop.fset is not None, "Codingstandards-Fehler: 'LibraryCard.member' muss einen @setter besitzen."

    # Loan properties
    borrow_date_prop = inspect.getattr_static(Loan, "borrow_date", None)
    assert isinstance(borrow_date_prop, property), "Codingstandards-Fehler: 'Loan.borrow_date' muss als @property gekapselt sein."
    assert borrow_date_prop.fset is not None, "Codingstandards-Fehler: 'Loan.borrow_date' muss einen @setter besitzen."

    duration_prop = inspect.getattr_static(Loan, "duration", None)
    assert isinstance(duration_prop, property), "Codingstandards-Fehler: 'Loan.duration' muss als @property gekapselt sein."
    assert duration_prop.fset is not None, "Codingstandards-Fehler: 'Loan.duration' muss einen @setter besitzen."

    due_date_prop = inspect.getattr_static(Loan, "due_date", None)
    assert isinstance(due_date_prop, property), "Codingstandards-Fehler: 'Loan.due_date' muss als @property gekapselt sein."
    assert due_date_prop.fset is None, "Codingstandards-Fehler: 'Loan.due_date' darf keinen Setter haben (read-only berechnet)."


def test_docstrings_presence():
    """Verifies that all modules, classes, properties, and methods have descriptive docstrings."""
    modules = [exceptions, book, loan, library_card, member, library]
    for mod in modules:
        assert mod.__doc__ and mod.__doc__.strip(), f"Codingstandards-Fehler: Modul-Docstring fehlt in '{mod.__name__}'."

    classes = [Book, Loan, LibraryCard, Member, Library, exceptions.LibraryError, exceptions.LoanLimitExceededError, exceptions.InvalidDurationError]
    for cls in classes:
        assert cls.__doc__ and cls.__doc__.strip(), f"Codingstandards-Fehler: Klassen-Docstring fehlt in Klasse '{cls.__name__}'."

        for attr_name, attr_obj in inspect.getmembers(cls):
            if not attr_name.startswith("_"):
                if inspect.isfunction(attr_obj):
                    assert attr_obj.__doc__ and attr_obj.__doc__.strip(), (
                        f"Codingstandards-Fehler: Methoden-Docstring fehlt bei '{cls.__name__}.{attr_name}'."
                    )
                elif isinstance(attr_obj, property):
                    assert attr_obj.__doc__ and attr_obj.__doc__.strip(), (
                        f"Codingstandards-Fehler: Property-Docstring fehlt bei '{cls.__name__}.{attr_name}'."
                    )


def test_naming_conventions():
    """Verifies PascalCase for classes and snake_case for functions/methods."""
    classes = [Book, Loan, LibraryCard, Member, Library, exceptions.LibraryError, exceptions.LoanLimitExceededError, exceptions.InvalidDurationError]
    for cls in classes:
        assert cls.__name__[0].isupper(), f"Klassenname '{cls.__name__}' muss gemäss PEP 8 in PascalCase geschrieben sein."

        for attr_name, attr_obj in inspect.getmembers(cls):
            if not attr_name.startswith("__") and (inspect.isfunction(attr_obj) or isinstance(attr_obj, property)):
                assert attr_name.islower() or "_" in attr_name, (
                    f"Methodenname '{cls.__name__}.{attr_name}' muss gemäss PEP 8 in snake_case geschrieben sein."
                )


def test_pylint_standards():
    """Runs pylint using the BZZ rcfile and checks for full compliance."""
    files = [
        "exceptions.py",
        "book.py",
        "loan.py",
        "library_card.py",
        "member.py",
        "library.py",
    ]
    cmd = [
        sys.executable,
        "-m",
        "pylint",
        "--rcfile=.github/autograding/pylintrc",
    ] + files

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    issues = [
        line for line in result.stdout.splitlines()
        if line
        and not line.startswith("*")
        and not line.startswith("-")
        and "Your code has been rated" not in line
    ]
    assert not issues, "Codingstandards-Verletzung durch Pylint festgestellt:\n" + "\n".join(issues)
