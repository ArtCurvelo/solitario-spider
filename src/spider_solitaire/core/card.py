
from dataclasses import dataclass
from enum import Enum


class Suit(Enum):
    SPADES = "espadas"
    HEARTS = "copas"
    DIAMONDS = "ouros"
    CLUBS = "paus"


class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


@dataclass
class Card:
    suit: Suit
    rank: Rank
    face_up: bool = False

    @property
    def value(self) -> int:
        return self.rank.value

    @property
    def is_face_up(self) -> bool:
        return self.face_up

    def reveal(self) -> None:
        self.face_up = True

    def hide(self) -> None:
        self.face_up = False
