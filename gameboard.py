class Gameboard:
    def __init__(self):
        self.gameboard = [0][0]
        self.make_gameboard


    def make_gameboard(self):
        cols = 20
        rows = 20
        self.gameboard = [[0] * cols] * rows

        for row in self.gameboard:
            print(row)
        