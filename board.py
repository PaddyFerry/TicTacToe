import copy


class Board:
    """A 3x3 tic tac toe board"""
    def __init__(self):
        self.tiles = [["-", "-", "-"] for _ in range(3)]
        self.empty = list(range(1, 10))
        self.locations = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        self.winning_pos = [(1, 2, 3),
                            (4, 5, 6),
                            (7, 8, 9),
                            (1, 4, 7),
                            (2, 5, 8),
                            (3, 6, 9),
                            (1, 5, 9),
                            (3, 5, 7)]

    def check_win(self):
        """Checks if there is a win condition in the board state
        :return: "X", "O" or None
        """
        win = None
        for pos in self.winning_pos:
            win = self.is_match(set(self.get_cells(pos)))
            if win:
                return win
        if not self.open_tiles():
            return "Draw"
        return win

    def get_cells(self, coords):
        """
        :param coords: list of (X,Y) tuples
        :return: list of values at each of coords
        """
        values = [self.locations[co] for co in coords]
        return [self.tiles[x][y] for x, y in values]

    @staticmethod
    def is_match(cells):
        """
        Checks if 3 values are a match
        :return: "X", "0", None
        """
        if len(cells) == 1 and "-" not in cells:
            return list(cells)[0]
        return None

    def play_tile(self, value, location):
        """Change tile value at location if tile is empty"""
        if location in self.empty:
            x, y = self.locations[location]
            self.tiles[x][y] = value
            self.empty[location-1] = 0
            return 1
        return 0

    def open_tiles(self):
        """Return open tile numbers"""
        return list(filter(None, self.empty))

    def __copy__(self):
        new = Board()
        new.tiles = copy.deepcopy(self.tiles)
        new.empty = copy.deepcopy(self.empty)
        return new

    def __repr__(self):
        view = ""
        for line in self.tiles:
            for cell in line:
                view += cell + " "
            view += "\n"
        return view
