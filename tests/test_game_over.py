
import pytest

from spider_solitaire.core.card import Card, Rank, Suit
from spider_solitaire.core.game import Game
from spider_solitaire.core.moves import move_cards, deal_from_stock


def test_cannot_move_cards_after_victory():
    game = Game()

    moving_card = Card(Suit.SPADES, Rank.FIVE, face_up=True)
    target_card = Card(Suit.HEARTS, Rank.SIX, face_up=True)

    game.columns[0] = [moving_card]
    game.columns[1] = [target_card]
    game.won = True

    with pytest.raises(ValueError, match="encerrada"):
        move_cards(game, 0, 1)

    assert game.columns[0] == [moving_card]
    assert game.columns[1] == [target_card]
    assert game.score == 500


def test_cannot_deal_from_stock_after_victory():
    game = Game()

    card = Card(Suit.SPADES, Rank.ACE, face_up=True)
    game.columns = [[card.copy() if hasattr(card, "copy") else card]
                    for _ in range(game.COLUMN_COUNT)]
    game.stock = [
        Card(Suit.HEARTS, Rank.ACE, face_up=False)
        for _ in range(game.COLUMN_COUNT)
    ]
    game.won = True

    original_stock = game.stock.copy()
    original_columns = [column.copy() for column in game.columns]

    with pytest.raises(ValueError, match="encerrada"):
        deal_from_stock(game)

    assert game.stock == original_stock
    assert game.columns == original_columns
