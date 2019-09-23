from bot import Bot
from board import Board
import pytest


@pytest.fixture()
def winning_o():
    """Example board with potential bot win"""
    board = Board()
    board.tiles = [["O", "-", "-"],
                   ["X", "-", "-"],
                   ["X", "-", "O"]]
    board.empty = [0, 2, 3, 0, 5, 6, 0, 8, 0]
    return board


@pytest.fixture()
def winning_x():
    """Example board with potential bot win"""
    board = Board()
    board.tiles = [["X", "-", "O"],
                   ["-", "-", "O"],
                   ["X", "O", "X"]]
    board.empty = [0, 2, 0, 4, 5, 0, 0, 0, 0]
    return board


@pytest.fixture()
def draw():
    """Example board with potential bot win"""
    board = Board()
    board.tiles = [["X", "-", "O"],
                   ["O", "X", "X"],
                   ["X", "O", "O"]]
    board.empty = [0, 2, 0, 0, 0, 0, 0, 0, 0]
    return board


def test_play_random_tile():
    b = Board()
    bot = Bot("O")
    b.play_tile(bot.symbol, bot.choose_tile(b))
    assert len(b.open_tiles()) == 8


def test_go_for_win_o(winning_o):
    bot = Bot("O")
    assert bot.choose_tile(winning_o) == 5


def test_block_win_o(winning_x):
    bot = Bot("O")
    assert bot.choose_tile(winning_x) == 4


def test_draw_o(draw):
    bot = Bot("O")
    assert bot.choose_tile(draw) == 2


def test_go_for_win_x(winning_x):
    bot = Bot("X")
    assert bot.choose_tile(winning_x) == 4


def test_block_win_x(winning_o):
    bot = Bot("X")
    assert bot.choose_tile(winning_o) == 5


def test_draw_x(draw):
    bot = Bot("X")
    assert bot.choose_tile(draw) == 2
