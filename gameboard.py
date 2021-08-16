class Gameboard:
    def __init__(self):
        self.gameboard = [0][0]
        self.make_gameboard


    def make_gameboard(self):
        cols = 11
        rows = 11
      
        #Make Gameboard 2d Array
        self.gameboard = [["." for i in range(cols)] for j in range(rows)]
       
        #Label Columns
        i = 0
        while i < 11:
            self.gameboard[i][0] = i
            i += 1

        #Label Rows
        i = 0
        while i < 11:
            self.gameboard[0][i] = i
            i += 1
        
        self.print_gameboard()     
            
    def print_gameboard(self):
             #Print Gameboard
        for row in self.gameboard:
            mx= 3
            print(" ".join(["{:<{mx}}".format(ele,mx=mx) for ele in row])) #Formats rows to be 3 characters wide