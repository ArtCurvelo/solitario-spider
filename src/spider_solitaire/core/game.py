
from spider_solitaire.core.card import Card
from spider_solitaire.core.deck import Deck


class Game:
    COLUMN_COUNT = 10
    INITIAL_FACE_UP = 1

    def __init__(self):
        self.deck = Deck()
        self.columns: list[list[Card]] = [
            [] for _ in range(self.COLUMN_COUNT)
        ]
        self.stock: list[Card] = []
        self.completed_sequences: list[list[Card]] = []

    def new_game(self) -> None:
        self.deck.reset()
        self.deck.shuffle()

        self.columns = [
            [] for _ in range(self.COLUMN_COUNT)
        ]
        self.stock = []
        self.completed_sequences = []

        for column_index, column in enumerate(self.columns):
            cards_to_deal = 6 if column_index < 4 else 5

            for card_index in range(cards_to_deal):
                card = self.deck.draw()

                if card_index == cards_to_deal - 1:
                    card.reveal()

                column.append(card)

        self.stock = self.deck.cards.copy()
        self.deck.cards.clear()

    @property
    def remaining_stock(self) -> int:
        return len(self.stock)
