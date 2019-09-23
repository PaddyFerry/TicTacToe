import re


class Player:
    """Player class that takes input from users"""
    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def choose_tile(board=None):
        """Asks user for tile number they would like to play. Valid nums between 1-9"""
        num = input("Choose tile: ").strip()
        match = re.match(r"^\d$", num)
        if match and 1 <= int(num) <= 9:
            num = int(num)
            return num
        return None

    @staticmethod
    def play_again():
        """Asks user if they would like to play again. Asks 3 times if bad input"""
        for _ in range(0, 3):
            play = input("Would you like to play again? (Y/N)").strip()
            match = re.match(r"^([YyNn])$", play)
            if match and play.lower() == "y":
                return True
            if match and play.lower() == "n":
                return False
        return False

    def __str__(self):
        return "Patrick"
