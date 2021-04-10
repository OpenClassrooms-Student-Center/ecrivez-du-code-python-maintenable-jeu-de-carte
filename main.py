"""Entry point."""

from models.deck import Deck

from controllers.base import Controller
from controllers.evaluate import CheckerRankAndSuitIndex

from views.base import Views
from views.player import PlayerView
from views.broadcast import BroadcastView
from views.internet import InternetStreamingView


def main():
    deck = Deck()

    active_view = PlayerView()
    passive_views = (active_view, BroadcastView(), InternetStreamingView())
    views = Views(active_view, passive_views)

    checker = CheckerRankAndSuitIndex()

    game = Controller(deck, views, checker)
    game.run()


if __name__ == "__main__":
    main()
