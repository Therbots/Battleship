from player import Player
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


    

    def run_game(self):
        pass
       

        
        