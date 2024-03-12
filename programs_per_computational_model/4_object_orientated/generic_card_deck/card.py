from suit import Suit


class Card:
    number = 0
    suit = None

    def __init__(self, number, suit):
        self.number = number
        if Suit.has_value(suit):
            self.suit = suit
        else:
            raise Exception(f"Invalid suit supplied {suit}")

    def __str__(self):
        return f"{self.suit} : {self.number}"
