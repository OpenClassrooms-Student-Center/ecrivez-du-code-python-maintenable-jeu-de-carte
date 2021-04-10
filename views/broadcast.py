"""Define the Broadcast view."""


class BroadcastView:
    """Broadcast on TV."""

    def prompt_for_player(self):
        return None

    def show_player_hand(self, name, hand):
        card = hand[0]
        card = card if card.is_face_up else "carte face cachée"
        print(f"[TV] {name} -> {card}")

    def prompt_for_flip_cards(self):
        return True

    def show_winner(self, name):
        print(f"[TV] {name} a gagné !")

    def prompt_for_new_game(self):
        return True
