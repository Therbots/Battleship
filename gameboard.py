class Gameboard:
    def __init__(self):
        self.gameboard = [0][0]
        self.make_gameboard


    def make_gameboard(self):
        cols = 21
        rows = 21
        # self.gameboard = [[0] * cols] * rows
        self.gameboard = [[0 for i in range(cols)] for j in range(rows)]
        i = 0
        while i < 21:
            self.gameboard[i][0] = i
            i += 1
        self.gameboard = [[0 for i in range(cols)] for j in range(rows)]
        i = 0
        while i < 21:
            self.gameboard[0][i] = i
            i += 1
        

        for row in self.gameboard:
            print(row)
        