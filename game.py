from player import Player
from gameboard import Gameboard



class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()


    def run_game(self):
        self.player_one.set_pieces()
       

        
        