from player import Player
from player2 import Player_2
from gameboard import Gameboard



class Game:
    def __init__(self):
        self.make_gameboards()

    def make_gameboards(self):
        gameboard_p1_self = Gameboard()
        gameboard_p1_opp = Gameboard()
        gameboard_p2_self = Gameboard()
        gameboard_p2_opp =Gameboard()
        gameboard_p1_self.make_gameboard()
        gameboard_p1_opp.make_gameboard()
        gameboard_p2_self.make_gameboard()
        gameboard_p2_opp.make_gameboard()

    def set_pieces(self):
        self.orientation = input("Do you want to place your ship 'horizontal' or 'vertical'? ")
        if self.orientation == 'horizontal':
            row_coordinates = input('Enter the row number that you want your ship placed: ')
            col_coordinates = input('Enter the columm number that you want your ship to be placed: ')

        self.coordinates


    

    def run_game(self):
        pass
       

        
        