from player import Player
from gameboard import Gameboard



class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()


    def run_game(self):
        self.player_one.set_pieces()
        self.player_two.set_pieces()

    def game_turn(self):



        # while(gameover):
            #Player 1 turn
            player1_turn_row =input("Player 1 enter row for attack: ")
            player1_turn_col = input("Player 1 enter column for attack: ")
            if(self.player_two.gameboard_self[player1_turn_row][player1_turn_col] == "o"):
                self.player_one.gameboard_opp[player1_turn_row][player1_turn_col] = "x"
                self.player_two.gameboard_self[player1_turn_row][player1_turn_col] = "x"
            
            #Player 2 turn
            player2_turn_row =input("Player 2 enter row for attack: ")
            player2_turn_col = input("Player 2 enter column for attack: ")
            if(self.player_one.gameboard_self[player2_turn_row][player2_turn_col] == "o"):
                self.player_two.gameboard_opp[player2_turn_row][player2_turn_col] = "x"
                self.player_one.gameboard_self[player2_turn_row][player2_turn_col] = "x"




        
        