
import pytest

from spider_solitaire.core.card import Card, Rank, Suit
from spider_solitaire.core.game import Game
from spider_solitaire.core.moves import check_completed_sequences


def create_complete_sequence(suit: Suit) -> list[Card]:
    return [
        Card(suit=suit, rank=Rank(value), face_up=True)
        for value in range(13, 0, -1)
    ]



def test_complete_sequence_is_removed_from_column():
    game = Game()
    sequence = create_complete_sequence(Suit.SPADES)
    expected_sequence = sequence.copy()
    game.columns[0] = sequence

    check_completed_sequences(game)

    assert game.columns[0] == []
    assert len(game.completed_sequences) == 1
    assert game.completed_sequences[0] == expected_sequence



def test_incomplete_sequence_is_not_removed():
    game = Game()
    sequence = create_complete_sequence(Suit.HEARTS)[:-1]
    game.columns[0] = sequence

    check_completed_sequences(game)

    assert game.columns[0] == sequence
    assert game.completed_sequences == []


def test_sequence_with_mixed_suits_is_not_removed():
    game = Game()
    sequence = create_complete_sequence(Suit.SPADES)
    sequence[5].suit = Suit.HEARTS
    game.columns[0] = sequence

    check_completed_sequences(game)

    assert game.columns[0] == sequence
    assert game.completed_sequences == []


def test_completed_sequence_reveals_card_below_it():
    game = Game()
    hidden_card = Card(Suit.CLUBS, Rank.FIVE, face_up=False)
    sequence = create_complete_sequence(Suit.DIAMONDS)
    game.columns[0] = [hidden_card] + sequence

    check_completed_sequences(game)

    assert game.columns[0] == [hidden_card]
    assert hidden_card.is_face_up



def test_valid_move_automatically_removes_completed_sequence():
    from spider_solitaire.core.moves import move_cards

    game = Game()
    sequence = create_complete_sequence(Suit.SPADES)

    game.columns[0] = [sequence[-1]]
    game.columns[1] = sequence[:-1]

    move_cards(game, 0, 1)

    assert game.columns[1] == []
    assert len(game.completed_sequences) == 1
    assert game.completed_sequences[0] == sequence
