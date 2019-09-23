import random
from copy import copy
from player import Player


class Bot(Player):
    """A bot class that extends player with very basic ai"""
    def choose_tile(self, board=None):
        """Read the board and if no good move can be seen then play a random tile"""
        move = self.read_board(board)
        if move:
            return move
        choice = random.choice(board.open_tiles()) if board.open_tiles() else 5
        return choice

    def read_board(self, board):
        """Creates copies of the board state to look into potential moves and return the best move
        This function will prioritize a win, then a block and otherwise will return none.
        """
        moves = board.open_tiles()
        blocks = []
        opp_sym = "O" if self.symbol == "X" else "X"
        for i, item in enumerate(moves):
            bot_move = copy(board)
            opp_move = copy(board)
            bot_move.play_tile(self.symbol, item)
            opp_move.play_tile(opp_sym, item)
            win = bot_move.check_win()
            loss = opp_move.check_win()
            if win == self.symbol:
                return moves[i]
            if loss == opp_sym:
                blocks.append(moves[i])
        if blocks:
            return blocks[0]
        return None

    @staticmethod
    def play_again():
        return False
