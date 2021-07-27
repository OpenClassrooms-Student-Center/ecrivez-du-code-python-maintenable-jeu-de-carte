"""Define the evaluation classes."""

from typing import List

from models.card import RANKS, SUITS
from models.player import Player


class CheckerRankAndSuitIndex:
    """Check the cards according to their rank and sequence."""

    def check(self, players: List[Player]):
        """Start the evaluation."""
        best_candidate = players[0]

        for player in players[1:]:
            player_card = player.hand[0]
            best_candidate_card = best_candidate.hand[0]

            score = (RANKS.index(player_card.rank), SUITS.index(player_card.suit))
            best_score = (
                RANKS.index(best_candidate_card.rank),
                SUITS.index(best_candidate_card.suit),
            )

            if score[0] == best_score[0]:
                if score[1] > best_score[1]:
                    best_candidate = player
            elif score[0] > best_score[0]:
                best_candidate = player

        return best_candidate.name
