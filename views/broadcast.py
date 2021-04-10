"""Define the Broadcast view."""


class BroadcastView:
    """Broadcast on TV."""

    def show_player_hand(self, name, hand):
        card = hand[0]
        card = card if card.is_face_up else "carte face cachée"
        print(f"[TV] {name} -> {card}")

    def show_winner(self, name):
        print(f"[TV] {name} a gagné !")
