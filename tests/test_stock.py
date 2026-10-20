
import pytest

from spider_solitaire.core.card import Card, Rank, Suit
from spider_solitaire.core.game import Game


def create_card(rank: Rank) -> Card:
    return Card(suit=Suit.SPADES, rank=rank, face_up=False)


def create_ready_game() -> Game:
    game = Game()

    game.columns = [
        [Card(Suit.SPADES, Rank.ACE, face_up=True)]
        for _ in range(10)
    ]

    game.stock = [
        create_card(Rank((index % 13) + 1))
        for index in range(10)
    ]

    return game


def test_stock_deal_adds_one_card_to_each_column():
    game = create_ready_game()
    original_sizes = [len(column) for column in game.columns]

    # A função de distribuição será implementada na próxima etapa.
    from spider_solitaire.core.moves import deal_from_stock

    deal_from_stock(game)

    assert [len(column) for column in game.columns] == [
        size + 1 for size in original_sizes
    ]
    assert len(game.stock) == 0
    assert all(column[-1].is_face_up for column in game.columns)


def test_stock_cannot_be_dealt_when_a_column_is_empty():
    game = create_ready_game()
    game.columns[3] = []
    original_stock = game.stock.copy()

    from spider_solitaire.core.moves import deal_from_stock

    with pytest.raises(ValueError):
        deal_from_stock(game)

    assert game.stock == original_stock
    assert game.columns[3] == []
