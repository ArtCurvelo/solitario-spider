
from spider_solitaire.core.card import Card


def can_place_card(card: Card, target: Card) -> bool:
    """Verifica se uma carta pode ser colocada sobre outra."""
    return target.value == card.value + 1


def is_valid_sequence(cards: list[Card]) -> bool:
    """Verifica se as cartas formam uma sequência móvel do mesmo naipe."""
    if not cards:
        return False

    if any(not card.is_face_up for card in cards):
        return False

    for current, following in zip(cards, cards[1:]):
        if current.suit != following.suit:
            return False

        if current.value != following.value + 1:
            return False

    return True
