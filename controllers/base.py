"""Define the main controller."""

from typing import List

from models.deck import Deck
from models.player import Player


class Controller:
    """Main controller."""

    def __init__(self, deck: Deck, view, checker_strategy):
        """Has a deck, a list of players and a view."""
        # models
        self.players: List[Player] = []
        self.deck = deck

        # views
        self.view = view

        # check strategy
        self.checker_strategy = checker_strategy

    def get_players(self):
        while len(self.players) < 5:  # nombre magique
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name)
            self.players.append(player)

    def evaluate_game(self):
        """Evaluate the game."""
        return self.checker_strategy.check(self.players)

    def rebuild_deck(self):
        """Rebuild the deck."""
        for player in self.players:
            while player.hand:
                card = player.hand.pop()
                card.is_face_up = False
                self.deck.append(card)
        self.deck.shuffle()

    def start_game(self):
        """Shuffle the deck and makes the players draw a card."""
        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            if card:
                player.hand.append(card)

    def run(self):
        self.get_players()

        running = True
        while running:
            self.start_game()

            for player in self.players:
                self.view.show_player_hand(player.name, player.hand)

            self.view.prompt_for_flip_cards()

            for player in self.players:
                for card in player.hand:
                    card.is_face_up = True
                self.view.show_player_hand(player.name, player.hand)

            self.view.show_winner(self.evaluate_game())

            running = self.view.prompt_for_new_game()
            self.rebuild_deck()
