"""Tests for Member class and 1:1 bidirectional relationship in constructor."""
import pytest

from library_card import LibraryCard
from member import Member


@pytest.fixture
def card():
    """Returns a LibraryCard fixture."""
    return LibraryCard()


@pytest.fixture
def member(card):
    """Returns a Member fixture linked with the card."""
    return Member("Anna Meier", card)


def test_member_initialisation(member, card):
    """Tests Member constructor sets name, card, and library is None."""
    assert member.name == "Anna Meier"
    assert member.card is card
    assert member.library is None


def test_bidirectional_relationship_in_constructor(member, card):
    """Tests that Member constructor establishes bidirectional link: card.member is member."""
    assert card.member is member
    assert member.card.member is member


def test_show_card(member, card):
    """Tests show_card method returns the library card."""
    assert member.show_card() is card


def test_library_setter(member):
    """Tests setting library on member."""
    fake_library = object()
    member.library = fake_library
    assert member.library is fake_library
