
import pytest

from spider_solitaire.core.card import Card, Rank, Suit
from spider_solitaire.core.game import Game
from spider_solitaire.core.moves import (
    check_completed_sequences,
    move_cards,
)


def create_complete_sequence(suit: Suit) -> list[Card]:
    return [
        Card(suit=suit, rank=Rank(value), face_up=True)
        for value in range(13, 0, -1)
    ]


def test_game_starts_with_initial_score():
    game = Game()

    assert game.score == 500


def test_register_move_decreases_score():
    game = Game()

    game.register_move()

    assert game.score == 499


def test_completed_sequence_increases_score():
    game = Game()

    game.register_completed_sequence()

    assert game.score == 600


def test_new_game_resets_score_and_victory():
    game = Game()
    game.score = 250
    game.won = True

    game.new_game()

    assert game.score == 500
    assert game.won is False


def test_eight_completed_sequences_win_the_game():
    game = Game()
    game.completed_sequences = [[] for _ in range(8)]

    game.register_completed_sequence()

    assert game.score == 600
    assert game.is_won is True


def test_valid_move_decreases_score():
    game = Game()

    moving_card = Card(Suit.SPADES, Rank.FIVE, face_up=True)
    target_card = Card(Suit.HEARTS, Rank.SIX, face_up=True)

    game.columns[0] = [moving_card]
    game.columns[1] = [target_card]

    move_cards(game, 0, 1)

    assert game.score == 499
    assert game.columns[1] == [target_card, moving_card]


def test_invalid_move_does_not_decrease_score():
    game = Game()

    moving_card = Card(Suit.SPADES, Rank.FIVE, face_up=True)
    target_card = Card(Suit.HEARTS, Rank.KING, face_up=True)

    game.columns[0] = [moving_card]
    game.columns[1] = [target_card]

    with pytest.raises(ValueError):
        move_cards(game, 0, 1)

    assert game.score == 500
    assert game.columns[0] == [moving_card]
    assert game.columns[1] == [target_card]


def test_completed_sequence_rewards_points_only_once():
    game = Game()
    sequence = create_complete_sequence(Suit.SPADES)
    game.columns[0] = sequence.copy()

    check_completed_sequences(game)
    check_completed_sequences(game)

    assert game.score == 600
    assert len(game.completed_sequences) == 1
