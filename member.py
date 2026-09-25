"""Member module representing a library member."""
from library_card import LibraryCard


class Member:
    """Represents a library member.

    Maintains a bidirectional 1:1 relationship with LibraryCard established in constructor,
    and a bidirectional 1:n relationship with Library established outside constructor.
    """

    def __init__(self, name: str, card: LibraryCard):
        """Initializes member and establishes bidirectional link with card.

        :param name: Name of the member.
        :param card: LibraryCard instance for this member.
        """
        # TODO: Store name, card, and set library to None.
        # TODO: Establish bidirectional relationship with card if card.member is not self
        raise NotImplementedError("Member.__init__ not implemented yet.")

    def show_card(self) -> LibraryCard:
        """Returns the member's library card."""
        # TODO: Return self._card
        raise NotImplementedError("Member.show_card not implemented yet.")

    @property
    def name(self) -> str:
        """Returns the member's name."""
        # TODO: Return internal name
        raise NotImplementedError("Member.name getter not implemented yet.")

    @property
    def card(self) -> LibraryCard:
        """Returns the member's library card."""
        # TODO: Return internal card
        raise NotImplementedError("Member.card getter not implemented yet.")

    @property
    def library(self):
        """Returns the library this member belongs to, or None."""
        # TODO: Return internal library
        raise NotImplementedError("Member.library getter not implemented yet.")

    @library.setter
    def library(self, value):
        """Sets the library for this member (called by Library.add_member)."""
        # TODO: Set internal library
        raise NotImplementedError("Member.library setter not implemented yet.")
