"""Entry point."""

from models.deck import Deck
from controllers.base import Controller
from controllers.evaluate import CheckerRankAndSuitIndex
from views.base import View


def main():
    deck = Deck()
    view = View()
    checker = CheckerRankAndSuitIndex()
    game = Controller(deck, view, checker)
    game.run()


if __name__ == "__main__":
    main()
