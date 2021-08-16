from game_pieces import Game_Pieces
from gameboard import Gameboard

class Player:
    def __init__(self):
        self.game_pieces = Game_Pieces()
        self.make_gameboards()

    def make_gameboards(self):
        self.gameboard_self = Gameboard()
        self.gameboard_opp = Gameboard()       
        self.gameboard_self.make_gameboard()
        self.gameboard_opp.make_gameboard()
        
        
    def set_pieces(self):
        for ship in self.game_pieces.ship_list:
            self.orientation = input("Do you want to place your ship 'horizontal' or 'vertical'? ")
            if self.orientation == 'horizontal':
                row_coordinates = int(input('Enter the row number that you want your ship placed: '))
                col_coordinates = int(input('Enter the columm number that you want your ship to be placed: '))
                i = 0
                while i < ship.size:
                    # self.gameboard_self[row_coordinates][col_coordinates + i] = 'o'
                    self.gameboard_self.gameboard[row_coordinates][col_coordinates + i] = 'o'
                    i += 1
                self.gameboard_self.print_gameboard()                


            else:
                
                row_coordinates = int(input('Enter the row number that you want your ship placed: '))
                col_coordinates = int(input('Enter the columm number that you want your ship to be placed: '))
                i = 0
                while i < ship.size:
                    # self.gameboard_self[row_coordinates][col_coordinates + i] = 'o'
                    self.gameboard_self.gameboard[row_coordinates + i][col_coordinates] = 'o'
                    i += 1
                self.gameboard_self.print_gameboard()  
    


    