
from spider_solitaire.core.card import Card
from spider_solitaire.core.deck import Deck


class Game:
    COLUMN_COUNT = 10
    INITIAL_FACE_UP = 1

    INITIAL_SCORE = 500
    MOVE_COST = 1
    SEQUENCE_REWARD = 100
    TOTAL_SEQUENCES = 8

    def __init__(self):
        self.deck = Deck()
        self.columns: list[list[Card]] = [
            [] for _ in range(self.COLUMN_COUNT)
        ]
        self.stock: list[Card] = []
        self.completed_sequences: list[list[Card]] = []

        self.score = self.INITIAL_SCORE
        self.won = False

    def new_game(self) -> None:
        self.deck.reset()
        self.deck.shuffle()

        self.columns = [
            [] for _ in range(self.COLUMN_COUNT)
        ]
        self.stock = []
        self.completed_sequences = []

        self.score = self.INITIAL_SCORE
        self.won = False

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

    @property
    def is_won(self) -> bool:
        return self.won

    def register_move(self) -> None:
        """Desconta pontos por um movimento válido."""
        self.score -= self.MOVE_COST

    def register_completed_sequence(self) -> None:
        """Premia uma sequência completa e verifica a vitória."""
        self.score += self.SEQUENCE_REWARD

        if len(self.completed_sequences) >= self.TOTAL_SEQUENCES:
            self.won = True
