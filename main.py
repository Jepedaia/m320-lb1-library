"""Main module demonstrating the Library Management System."""
from datetime import datetime, timedelta

from book import Book
from library import Library
from library_card import LibraryCard
from member import Member


def main():
    """Demonstrates creating library entities and borrowing books."""
    # 1. Create a Library
    city_library = Library("Stadtbibliothek BZZ")

    # 2. Create LibraryCards
    card_anna = LibraryCard()
    card_ben = LibraryCard()

    # 3. Create Members (establishes 1:1 bidirectional link in constructor)
    anna = Member("Anna Meier", card_anna)
    ben = Member("Ben Keller", card_ben)

    # 4. Add Members to Library (establishes 1:n bidirectional link outside constructor)
    city_library.add_member(anna)
    city_library.add_member(ben)

    print("=== Registered Members ===")
    print(city_library.show_member_list())

    # 5. Create Dataclass Books
    book1 = Book(title="Clean Code", author="Robert C. Martin", isbn="978-0132350884")
    book2 = Book(title="Design Patterns", author="Erich Gamma et al.", isbn="978-0201633610")
    book3 = Book(title="Fluent Python", author="Luciano Ramalho", isbn="978-1491946008")
    book4 = Book(title="Python Crash Course", author="Eric Matthes", isbn="978-1593279288")
    book5 = Book(title="Effective Python", author="Brett Slatkin", isbn="978-0134853987")
    book6 = Book(title="The Pragmatic Programmer", author="David Thomas", isbn="978-0201616224")

    # 6. Borrow books (successful borrows)
    print("=== Borrowing Books ===")
    city_library.borrow_book(anna, book1, days=14)
    city_library.borrow_book(anna, book2, days=21)
    city_library.borrow_book(anna, book3, days=30)
    city_library.borrow_book(anna, book4, days=14)
    city_library.borrow_book(anna, book5, days=7)

    # 7. Borrowing 6th book triggers LoanLimitExceededError (gracefully caught in Library.borrow_book)
    success = city_library.borrow_book(anna, book6, days=14)
    print(f"Anna borrow 6th book result: {success} (expected False due to limit)")

    # 8. Check overview
    print("\n=== Card Overview ===")
    print(anna.card.show_overview())

    # 9. Overdue check simulation
    future_date = datetime.now() + timedelta(days=25)
    print(f"Overdue loans for Anna in 25 days: {anna.card.count_overdue_loans(future_date)}")


if __name__ == "__main__":
    main()
