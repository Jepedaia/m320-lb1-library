from library_card import LibraryCard


class Member:

    def __init__(self, name: str, card: LibraryCard):
        # TODO: Store name, card, and set library to None.
        # TODO: Establish bidirectional relationship with card if card.member is not self
        raise NotImplementedError("Member.__init__ not implemented yet.")

    def show_card(self) -> LibraryCard:
        # TODO: Return card
        raise NotImplementedError("Member.show_card not implemented yet.")

    @property
    def name(self) -> str:
        # TODO: Return name
        raise NotImplementedError("Member.name getter not implemented yet.")

    @property
    def card(self) -> LibraryCard:
        # TODO: Return card
        raise NotImplementedError("Member.card getter not implemented yet.")

    @property
    def library(self):
        # TODO: Return library
        raise NotImplementedError("Member.library getter not implemented yet.")

    @library.setter
    def library(self, value):
        # TODO: Set library
        raise NotImplementedError("Member.library setter not implemented yet.")
