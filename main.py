"""Entry point."""

from models.deck import Deck
from controllers.base import Controller
from views.base import View


def main():
    deck = Deck()
    view = View()
    game = Controller(deck, view)
    game.run()


if __name__ == "__main__":
    main()
