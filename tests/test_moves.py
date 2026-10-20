
import pytest

from spider_solitaire.core.card import Card, Rank, Suit
from spider_solitaire.core.game import Game
from spider_solitaire.core.moves import move_cards


def create_card(suit: Suit, rank: Rank, face_up: bool = True) -> Card:
    return Card(suit=suit, rank=rank, face_up=face_up)


def create_game_with_columns(
    source_cards: list[Card],
    target_cards: list[Card],
) -> Game:
    game = Game()
    game.columns = [source_cards, target_cards] + [
        [] for _ in range(8)
    ]
    game.stock = []
    return game


def test_valid_move_preserves_card_count():
    seven = create_card(Suit.SPADES, Rank.SEVEN)
    eight = create_card(Suit.HEARTS, Rank.EIGHT)
    game = create_game_with_columns([seven], [eight])

    move_cards(game, 0, 1)

    assert game.columns[0] == []
    assert game.columns[1] == [eight, seven]


def test_invalid_move_does_not_change_columns():
    seven = create_card(Suit.SPADES, Rank.SEVEN)
    five = create_card(Suit.HEARTS, Rank.FIVE)
    game = create_game_with_columns([seven], [five])

    with pytest.raises(ValueError):
        move_cards(game, 0, 1)

    assert game.columns[0] == [seven]
    assert game.columns[1] == [five]


def test_move_reveals_new_top_card():
    hidden_six = create_card(Suit.SPADES, Rank.SIX, face_up=False)
    seven = create_card(Suit.SPADES, Rank.SEVEN)
    eight = create_card(Suit.HEARTS, Rank.EIGHT)
    game = create_game_with_columns([hidden_six, seven], [eight])

    move_cards(game, 0, 1)

    assert game.columns[0] == [hidden_six]
    assert hidden_six.is_face_up

def test_mixed_suit_sequence_cannot_move_as_a_group():
    seven = create_card(Suit.SPADES, Rank.SEVEN)
    six = create_card(Suit.HEARTS, Rank.SIX)
    eight = create_card(Suit.CLUBS, Rank.EIGHT)

    game = create_game_with_columns([seven, six], [eight])

    with pytest.raises(ValueError):
        move_cards(game, 0, 1, count=2)

    assert game.columns[0] == [seven, six]
    assert game.columns[1] == [eight]