"""Define the main controller."""

from typing import List

from models.deck import Deck
from models.player import Player


class Controller:
    """Main controller."""

    def __init__(self, deck: Deck, view):
        """Has a deck, a list of players and a view."""
        # models
        self.players: List[Player] = []
        self.deck = deck

        # views
        self.view = view

    def get_players(self):
        """Get some players."""
        while len(self.players) < 5:  # nombre magique
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name)
            self.players.append(player)

    def start_game(self):
        """Shuffle the deck and makes the players draw a card."""
        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            if card:
                player.hand.append(card)

    def run(self):
        """Run the game."""
        self.get_players()
        self.start_game()

        for player in self.players:
            self.view.show_player_hand(player.name, player.hand)
