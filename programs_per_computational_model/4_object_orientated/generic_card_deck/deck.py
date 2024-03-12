class Deck:
    cards = []
    _deck_size = 52

    def __init__(self, cards):
        if len(cards) == 52:
            self.cards = cards
        else:
            raise Exception(
                f"Incorrect number of cards supplied. Number supplied {len(cards)}"
            )

    def shuffle(self):
        return self.cards.reverse()

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards[0]
        else:
            raise Exception("No cards in deck")
