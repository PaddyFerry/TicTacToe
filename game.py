from board import Board
from bot import Bot
from player import Player


class Game:
    """Main game object. Controls game logic."""
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Bot("O")]
        self.winner = None

    def main_loop(self):
        """Main game loop that iterates through players"""
        while self.board.open_tiles():
            if self.winner:
                break
            for player in self.players:
                print(self.board)
                chosen_tile = self.board.play_tile(player.symbol, player.choose_tile(self.board))
                while not chosen_tile and self.board.open_tiles():
                    chosen_tile = self.board.play_tile(player.symbol, player.choose_tile(self.board))
                self.winner = self.board.check_win()
                if self.winner:
                    self.winner_seq()

    def winner_seq(self):
        """Prints the winner or draw. Asks player if they want to play again"""
        print(self.board)
        if self.winner == "Draw":
            print("It was a draw!")
        else:
            print(f"{self.winner} is the winner!")
        if self.players[0].play_again():
            self.board = Board()
            self.winner = None
        else:
            print("Thank you for playing!")


if __name__ == '__main__':
    NEW_GAME = Game()
    NEW_GAME.main_loop()
