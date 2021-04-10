"""Define the cards."""

SUITS = ("diamonds", "coeurs", "piques", "carreaux")
RANKS = (
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "valet",
    "reine",
    "roi",
    "ace",
)


class Card:
    """Card class.

    Has a suit and a rank.
    """

    def __init__(self, suit, rank):
        """Init the suit, the rank, is_face_up and the scores."""
        self.suit = suit
        self.rank = rank
        self.is_face_up = False

    def __str__(self):
        """Used in print."""
        return f"{self.rank} de {self.suit}"

    def __repr__(self):
        """Used in print."""
        return str(self)
