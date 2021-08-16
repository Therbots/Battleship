from player import Player
from gameboard import Gameboard
from game_pieces import Game_Pieces


class Game:
    def __init__(self):
        self.pieces = Game_Pieces()

    def run_game(self):
        gameboard_p1_self = Gameboard()
        gameboard_p1_opp = Gameboard()
        gameboard_p2_self = Gameboard()
        gameboard_p2_opp =Gameboard()
        gameboard_p1_self.make_gameboard()
        gameboard_p1_opp.make_gameboard()
        gameboard_p2_self.make_gameboard()
        gameboard_p2_opp.make_gameboard()

        
        