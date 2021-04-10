"""Player and Hand."""

from .card import Card


class Hand(list):
    """Player hand."""

    def append(self, object):
        """Append a card."""
        if not isinstance(object, Card):
            return ValueError("Vous ne pouvez ajouter que des cartes !")
        return super().append(object)


class Player:
    """Player."""

    def __init__(self, name):
        """Has a name and a hand."""
        self.name = name
        self.hand = Hand()
