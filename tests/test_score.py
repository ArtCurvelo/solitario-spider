
from spider_solitaire.core.game import Game


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
