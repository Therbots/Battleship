from ship import Ship

class Game_Pieces:
    def __init__(self):
        self.ship_list = []
        self.create_pieces()


    def create_pieces(self):
        destroyer = Ship("Destroyer", 2)
        submarine = Ship("Submarine", 3)
        battleship = Ship("Battleship", 4)
        aircraft_carrier = Ship("Aircraft Carrier", 5)
        self.ship_list.append(destroyer)
        self.ship_list.append(submarine)
        self.ship_list.append(battleship)
        self.ship_list.append(aircraft_carrier)

 

        


        
