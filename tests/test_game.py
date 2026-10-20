
from spider_solitaire.core.game import Game


def test_new_game_has_ten_columns():
    game = Game()
    game.new_game()

    assert len(game.columns) == 10


def test_new_game_deals_correct_number_of_cards():
    game = Game()
    game.new_game()

    assert [len(column) for column in game.columns] == [
        6, 6, 6, 6, 5, 5, 5, 5, 5, 5
    ]


def test_new_game_has_fifty_cards_in_stock():
    game = Game()
    game.new_game()

    assert game.remaining_stock == 50


def test_new_game_has_only_one_face_up_card_per_column():
    game = Game()
    game.new_game()

    for column in game.columns:
        assert sum(card.is_face_up for card in column) == 1


def test_new_game_accounts_for_all_104_cards():
    game = Game()
    game.new_game()

    cards_in_columns = sum(len(column) for column in game.columns)
    cards_in_completed_sequences = sum(
        len(sequence) for sequence in game.completed_sequences
    )

    assert (
        cards_in_columns
        + game.remaining_stock
        + cards_in_completed_sequences
    ) == 104
