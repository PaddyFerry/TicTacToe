from game import Game
from bot import Bot


def test_bot_game():
    g = Game()
    g.players = [Bot("X"), Bot("O")]
    g.main_loop()
    assert g.winner in ["X", "O", "Draw"]
