import pytest
from board import Board


# Fixtures
@pytest.fixture()
def win_col():
    """Example board with column win"""
    board = Board()
    board.tiles = [["X", "O", "O"],
                   ["X", "-", "-"],
                   ["X", "O", "-"]]
    return board


@pytest.fixture()
def win_row():
    """Example board with row win"""
    board = Board()
    board.tiles = [["O", "O", "O"],
                   ["-", "X", "O"],
                   ["X", "-", "X"]]
    return board


@pytest.fixture()
def win_diag():
    """Example board with diagonal win"""
    board = Board()
    board.tiles = [["X", "O", "O"],
                   ["O", "X", "-"],
                   ["X", "-", "X"]]
    return board


@pytest.fixture()
def draw():
    """Example board with potential bot win"""
    board = Board()
    board.tiles = [["X", "X", "O"],
                   ["O", "X", "X"],
                   ["X", "O", "O"]]
    board.empty = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    return board


def test_get_cells(win_col):
    """Check if correct cells are returned"""
    assert win_col.get_cells((1, 2, 3)) == ["X", "O", "O"]


# Row/Col/Diag Checking
def test_check_col_win(win_col):
    """Check if column win is recognised"""
    assert win_col.check_win() == "X"


def test_check_win_fail():
    """Assert that there is no win"""
    empty = Board()
    assert empty.check_win() is None


def test_check_win_row(win_row):
    """Check if row win is recognised"""
    assert win_row.check_win() == "O"


def test_check_win_diag_right(win_diag):
    """Check if right diagonal win is recognised"""
    assert win_diag.check_win() == "X"


def test_check_win_diag_left(win_diag):
    """Check if right diagonal win is recognised"""
    win_diag.tiles[0][0] = "0"
    win_diag.tiles[0][2] = "X"
    assert win_diag.check_win() == "X"


def test_check_win_draw(draw):
    assert draw.check_win() == "Draw"


def test_play_tile():
    """Test that tile is changed"""
    board = Board()
    board.play_tile("X", 1)
    assert board.play_tile("X", 5) == 1
    assert board.tiles == [["X", "-", "-"], ["-", "X", "-"], ["-", "-", "-"]]


def test_illegal_move():
    """Test that illegal move is not taken"""
    board = Board()
    board.play_tile("X", 1)
    assert board.play_tile("X", 1) == 0
    assert board.tiles == [["X", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def test_open_moves():
    """Assert that only open tiles are returned"""
    board = Board()
    board.play_tile("X", 1)
    board.play_tile("O", 2)
    board.play_tile("X", 7)
    board.play_tile("O", 5)
    assert board.open_tiles() == [3, 4, 6, 8, 9]


def test_full_board():
    """Check 0 is returned when board is full"""
    board = Board()
    for i in range(1, 10):
        board.play_tile("X", i)
    assert len(board.open_tiles()) == 0
