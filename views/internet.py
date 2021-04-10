"""Define the InternetStreamingView."""


class InternetStreamingView:
    """Stream on internet."""

    def show_player_hand(self, name, hand):
        card = hand[0]
        card = card if card.is_face_up else "carte face cachée"
        print(f"[Internet] {name} -> {card}")

    def show_winner(self, name):
        print(f"[Internet] {name} a gagné !")
