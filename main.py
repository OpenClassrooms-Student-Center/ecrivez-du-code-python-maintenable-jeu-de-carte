"""Entry point."""

from models.deck import Deck
from controllers.base import Controller
from controllers.evaluate import CheckerRankAndSuitIndex
from views.base import PlayerView
from views.broadcast import BroadcastView
from views.internet import InternetStreamingView


def main():
    deck = Deck()
    view = PlayerView()
    views = (view, BroadcastView(), InternetStreamingView())
    checker = CheckerRankAndSuitIndex()
    game = Controller(deck, view, views, checker)
    game.run()


if __name__ == "__main__":
    main()
