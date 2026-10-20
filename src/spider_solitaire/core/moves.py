
from spider_solitaire.core.game import Game
from spider_solitaire.core.rules import (
    can_place_card,
    is_valid_sequence,
)


def move_cards(
    game: Game,
    source_index: int,
    target_index: int,
    count: int = 1,
) -> None:
    """Move uma carta ou sequência entre duas colunas."""

    if source_index == target_index:
        raise ValueError("A origem e o destino devem ser diferentes.")

    if not 0 <= source_index < len(game.columns):
        raise ValueError("Coluna de origem invalida.")

    if not 0 <= target_index < len(game.columns):
        raise ValueError("Coluna de destino invalida.")

    source = game.columns[source_index]
    target = game.columns[target_index]

    if count < 1 or count > len(source):
        raise ValueError("Quantidade de cartas invalida.")

    moving_cards = source[-count:]

    if not is_valid_sequence(moving_cards):
        raise ValueError(
            "As cartas selecionadas nao formam uma sequencia valida."
        )

    if target and not can_place_card(moving_cards[0], target[-1]):
        raise ValueError("Movimento invalido para essa coluna.")

    target.extend(moving_cards)
    del source[-count:]

    if source and not source[-1].is_face_up:
        source[-1].reveal()

    game.register_move()
    check_completed_sequences(game)


def deal_from_stock(game: Game) -> None:
    """Distribui uma carta virada para cima em cada coluna."""

    if not game.stock:
        raise ValueError("O monte esta vazio.")

    if len(game.stock) < game.COLUMN_COUNT:
        raise ValueError("Nao ha cartas suficientes para distribuir.")

    if any(not column for column in game.columns):
        raise ValueError(
            "Todas as colunas precisam ter cartas antes da distribuicao."
        )

    for column in game.columns:
        card = game.stock.pop()
        card.reveal()
        column.append(card)


def check_completed_sequences(game: Game) -> None:
    """Remove sequencias completas do mesmo naipe, do Rei ao As."""

    expected_values = list(range(13, 0, -1))

    for column in game.columns:
        while len(column) >= 13:
            sequence = column[-13:]

            if not all(card.is_face_up for card in sequence):
                break

            if not all(
                card.suit == sequence[0].suit
                for card in sequence
            ):
                break

            if [card.value for card in sequence] != expected_values:
                break

            game.completed_sequences.append(sequence.copy())
            del column[-13:]

            game.register_completed_sequence()

            if column and not column[-1].is_face_up:
                column[-1].reveal()
