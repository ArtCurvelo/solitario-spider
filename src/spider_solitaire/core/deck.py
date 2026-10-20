
import random

from spider_solitaire.core.card import Card, Rank, Suit


class Deck:
    COPIES = 2

    def __init__(self):
        self.cards: list[Card] = []
        self.reset()

    def reset(self) -> None:
        self.cards = [
            Card(suit=suit, rank=rank)
            for _ in range(self.COPIES)
            for suit in Suit
            for rank in Rank
        ]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> Card:
        if not self.cards:
            raise ValueError("O baralho esta vazio.")

        return self.cards.pop()

    def __len__(self) -> int:
        return len(self.cards)
