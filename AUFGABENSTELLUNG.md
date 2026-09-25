# Leistungsbeurteilung 1 (LB1) – Vorbereitungsprojekt: Bibliotheksverwaltung (Library Management)

## 1. Ausgangslage & Kontext
Im Rahmen der Leistungsbeurteilung 1 im Modul M320 (Objektorientiertes Programmieren mit Python) vertiefen Sie den Umgang mit:
- **Objektbeziehungen** (einseitig/zweiseitig, 1:1, 1:n, im vs. ausserhalb des Konstruktors)
- **Listenverwaltung** (Elemente hinzufügen, auslesen, zählen, Limits überwachen)
- **Dataclasses** (Reine Dataclass & Dataclass mit Properties/Validierung)
- **Datum & Zeit** (`datetime` und `timedelta`)
- **Datenkapselung** (`@property` und `@setter`)
- **Exceptions** (eigene Exceptions definieren, auslösen mit `raise` und fangen mit `try/except`)
- **Codingstandards** (PEP 8 & BZZ-Codingstandards, englische Bezeichner)

In diesem Übungsprojekt implementieren Sie ein **Bibliotheksverwaltungssystem**. Das Projekt ist mit vollständigen Unittests (`pytest`) und Pylint-Checks ausgestattet. Ihre Aufgabe ist es, die vorbereiteten Methoden-Stubs schrittweise zu implementieren, bis alle Tests **grün** sind und die Codingstandards eingehalten werden.

---

## 2. UML-Klassendiagramm

```mermaid
classDiagram
    class LibraryError {
        <<Exception>>
    }
    class LoanLimitExceededError {
        <<Exception>>
    }
    class InvalidDurationError {
        <<Exception>>
    }
    LibraryError <|-- LoanLimitExceededError
    LibraryError <|-- InvalidDurationError

    class Book {
        <<dataclass>>
        +str title
        +str author
        +str isbn
    }

    class Loan {
        <<dataclass>>
        +Book book
        +datetime borrow_date
        +timedelta duration
        +datetime due_date
        +is_overdue(check_date: datetime) bool
    }

    class LibraryCard {
        -list~Loan~ _loans
        -Member _member
        +add_loan(loan: Loan) None
        +take_loan(index: int) Loan
        +count_loans() int
        +count_overdue_loans(current_date: datetime) int
        +show_overview() str
        +member Member
    }

    class Member {
        -str _name
        -LibraryCard _card
        -Library _library
        +name str
        +card LibraryCard
        +library Library
        +show_card() LibraryCard
    }

    class Library {
        -str _name
        -list~Member~ _members
        +name str
        +add_member(member: Member) None
        +take_member(index: int) Member
        +count_members() int
        +show_member_list() str
        +borrow_book(member: Member, book: Book, days: int) bool
        +find_member(name: str) Member
    }

    %% Relationships
    Library "1" o-- "0..50" Member : manages (zweiseitig 1:n,\nausserhalb Konstruktor)
    Member "1" <--> "1" LibraryCard : owns (zweiseitig 1:1,\nim Konstruktor)
    LibraryCard "1" *-- "0..5" Loan : contains (einseitig 1:n)
    Loan "1" --> "1" Book : refers to (einseitig 1:1)
```

---

## 3. Übersicht der Beziehungen (Prüfungsschwerpunkt!)

| Beziehung | Beteiligte Klassen | Art | Multiplizität | Wo/Wie hergestellt |
|---|---|---|---|---|
| **Ausleihe -> Buch** | `Loan` $\rightarrow$ `Book` | Einseitig | 1:1 | Im `Loan`-Objekt (`book`-Attribut) |
| **Karte -> Ausleihen** | `LibraryCard` $\rightarrow$ `Loan` | Einseitig | 1:n | Verwaltet in `self._loans: list` über `add_loan` |
| **Mitglied <-> Karte** | `Member` $\leftrightarrow$ `LibraryCard` | **Zweiseitig** | 1:1 | **Im Konstruktor** von `Member`: `card.member = self` |
| **Bibliothek <-> Mitglied** | `Library` $\leftrightarrow$ `Member` | **Zweiseitig** | 1:n | **Ausserhalb des Konstruktors**: in `Library.add_member()` via `member.library = self` |

---

## 4. Spezifikation der Module und Klassen

### 4.1 Modul `exceptions.py`
Hier werden domain-spezifische Exceptions definiert:
- `LibraryError(Exception)`: Basisklasse aller Bibliotheksfehler.
- `LoanLimitExceededError(LibraryError)`: Wird ausgelöst, wenn ein Mitglied mehr als 5 Bücher gleichzeitig ausleihen möchte.
- `InvalidDurationError(LibraryError)`: Wird ausgelöst, wenn eine Ausleihdauer ungültig ist ($\le 0$ oder $> 60$ Tage).

---

### 4.2 Modul `book.py`
Implementiert als reine `@dataclass`:
- **Attribute:**
  - `title: str`
  - `author: str`
  - `isbn: str`
- Generiert automatisch `__init__`, `__repr__` und `__eq__`.

---

### 4.3 Modul `loan.py`
Implementiert als `@dataclass` mit Kapselung (`property` / `setter`), `datetime` und `timedelta`:
- **Felder & Attribute:**
  - `book: Book`: Das ausgeliehene Buch.
  - `borrow_date: datetime | str | None`:
    - Standardwert: `None` (wird zu `datetime.now()`).
    - Setter akzeptiert entweder ein `datetime`-Objekt oder einen Datumsstring im Format `"%d.%m.%Y"` (z. B. `"15.10.2026"`). Leere Strings oder `None` setzen das aktuelle Datum (`datetime.now()`).
  - `duration: timedelta | int`:
    - Standardwert: `14` Tage.
    - Setter akzeptiert entweder ein `timedelta`-Objekt oder eine Ganzzahl (Tage), die in `timedelta(days=value)` konvertiert wird.
    - **Validierung:** Falls `duration.days <= 0` oder `duration.days > 60`, muss ein `InvalidDurationError` ausgelöst werden!
- **Berechnete Properties & Methoden:**
  - `@property due_date(self) -> datetime`:
    - Gibt das Fälligkeitsdatum zurück: `borrow_date + duration`.
  - `is_overdue(self, check_date: datetime | None = None) -> bool`:
    - Vergleicht `check_date` (falls `None`, `datetime.now()`) mit `self.due_date`.
    - Gibt `True` zurück, wenn `check_date > self.due_date`, sonst `False`.

---

### 4.4 Modul `library_card.py`
Verwaltet die aktiven Ausleihen eines Mitglieds:
- **Konstruktor:** `__init__(self, member=None)`:
  - Initialisiert eine leere Liste `self._loans = []`.
  - Speichert `self._member = member`.
- **Properties:**
  - `member`: Getter und Setter für das zugehörige `Member`-Objekt.
- **Methoden:**
  - `add_loan(self, loan: Loan) -> None`:
    - Prüft, ob bereits 5 Ausleihen vorhanden sind (`count_loans() >= 5`). Falls ja: `raise LoanLimitExceededError("Maximum number of loans reached (5)")`.
    - Falls `loan` noch nicht in `self._loans` enthalten ist, wird es hinzugefügt.
  - `take_loan(self, index: int) -> Loan`:
    - Gibt die Ausleihe am übergebenen `index` zurück.
    - Wirft `IndexError`, falls der Index ungültig ist (`index < 0` oder `index >= len(self._loans)`).
  - `count_loans(self) -> int`:
    - Gibt die Anzahl der aktuell aktiven Ausleihen zurück.
  - `count_overdue_loans(self, current_date: datetime | None = None) -> int`:
    - Zählt alle Ausleihen in `self._loans`, bei denen `loan.is_overdue(current_date)` `True` ergibt.
  - `show_overview(self) -> str`:
    - Gibt eine formatierte Zusammenfassung als String zurück (z. B. `"Card for Anna Meier: 3 loans"`).

---

### 4.5 Modul `member.py`
Repräsentiert ein Bibliotheksmitglied:
- **Konstruktor:** `__init__(self, name: str, card: LibraryCard)`:
  - Speichert `_name = name`, `_card = card` und setzt `_library = None`.
  - **Zweiseitige 1:1-Beziehung im Konstruktor:**
    Verknüpft die übergebene Karte sofort mit diesem Mitglied:
    ```python
    if self._card.member is not self:
        self._card.member = self
    ```
- **Properties:**
  - `name`: Read-only Property (nur Getter).
  - `card`: Read-only Property (nur Getter).
  - `library`: Getter und Setter (`@library.setter`).
- **Methoden:**
  - `show_card(self) -> LibraryCard`:
    - Gibt `self._card` zurück.

---

### 4.6 Modul `library.py`
Repräsentiert die Bibliothek:
- **Konstruktor:** `__init__(self, name: str)`:
  - Speichert `_name = name` und initialisiert eine leere Mitgliederliste `_members = []`.
- **Properties:**
  - `name`: Read-only Property.
- **Methoden:**
  - `add_member(self, member: Member) -> None`:
    - Wirft `OverflowError`, wenn die Maximalkapazität von 50 Mitgliedern erreicht ist.
    - Falls `member` noch nicht in `self._members` existiert:
      - Zur Liste hinzufügen: `self._members.append(member)`
      - **Zweiseitige 1:n-Beziehung ausserhalb des Konstruktors setzen:** `member.library = self`
  - `take_member(self, index: int) -> Member`:
    - Gibt das Mitglied am angegebenen Index zurück.
    - Wirft `IndexError`, wenn der Index ungültig ist.
  - `count_members(self) -> int`:
    - Gibt die Anzahl registrierter Mitglieder zurück.
  - `show_member_list(self) -> str`:
    - Gibt einen String zurück, der alle Mitgliedernamen zeilenweise enthält.
  - `find_member(self, name: str) -> Member | None`:
    - Sucht in `self._members` nach dem Namen und gibt das Mitglied zurück, oder `None`.
  - `borrow_book(self, member: Member, book: Book, days: int = 14) -> bool`:
    - **WICHTIG (Exception Handling / Fangen):**
      Erstellt ein `Loan`-Objekt und versucht, es mittels `member.card.add_loan(loan)` hinzuzufügen.
      Fängt `LoanLimitExceededError` ab!
      ```python
      try:
          loan = Loan(book=book, duration=days)
          member.card.add_loan(loan)
          return True
      except LoanLimitExceededError:
          print(f"Ausleihe fehlgeschlagen: {member.name} hat das Ausleihlimit erreicht.")
          return False
      ```

---

## 5. Codingstandards (BZZ-Richtlinien & PEP 8)
1. **Englische Bezeichner:**
   Alle Klassen-, Funktions-, Variablen- und Attributnamen müssen in englischer Sprache verfasst sein.
2. **Datenkapselung:**
   Private Attribute beginnen mit einem Unterstrich (z. B. `_loans`, `_members`, `_borrow_date`).
   Zugriffe erfolgen über `@property` und `@<attribut>.setter`.
3. **Docstrings:**
   Jedes Modul, jede Klasse und jede Methode besitzt einen aussagekräftigen Docstring.
4. **Formatierung:**
   4 Leerzeichen Einrückung, keine überflüssigen Imports, Leerzeilen gemäss PEP 8.

---

## 6. Überprüfung & Ausführung

### Unittests ausführen:
Im Projektverzeichnis `m320-lb1-library` ausführen:
```bash
/home/jepedaia/PycharmProjects/M320/m320-ix25-m320-lu09-a01-school-ia25b-grimaj/.venv/bin/pytest -v
```
(Oder bei aktivem venv einfach: `pytest -v`)

### Pylint-Prüfung ausführen:
```bash
python3 _run_pylint.py
```
Oder direkt:
```bash
/home/jepedaia/PycharmProjects/M320/m320-ix25-m320-lu09-a01-school-ia25b-grimaj/.venv/bin/pylint --rcfile .github/autograding/pylintrc exceptions.py book.py loan.py library_card.py member.py library.py
```

### Hauptprogramm ausführen:
```bash
python3 main.py
```

---

## 7. Empfohlene Reihenfolge zur Bearbeitung
1. `exceptions.py` (bereits vorbereitet, inspizieren)
2. `book.py` (`@dataclass` Attribute prüfen)
3. `loan.py` (Properties, Datums- und Timedelta-Konvertierung, Fälligkeitsberechnung)
4. `library_card.py` (Listenverwaltung, Limits, Exceptions)
5. `member.py` (1:1-Beziehung im Konstruktor)
6. `library.py` (1:n-Beziehung ausserhalb Konstruktor, `try/except` in `borrow_book`)
7. `main.py` ausführen und `pytest -v` überprüfen!
