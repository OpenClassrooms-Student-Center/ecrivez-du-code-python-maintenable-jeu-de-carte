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

    def evaluate_game(self):
        """Evaluate the best player."""
        last_player = self.players[0]
        best_candidate = self.players[0]

        for player in self.players[1:]:
            player_card = player.hand[0]
            last_player_card = last_player.hand[0]

            if player_card > last_player_card:
                best_candidate = player

            last_player = player

        return best_candidate.name

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
        """Run the game."""
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
