

class Board:

    def __init__(self, rows, columns, win_len):
        
        self.rows = rows                            #
        self.columns = columns                      #
        self.win_len = win_len                      #

        self.grid = [[' ' for i in range (columns)] for j in range (rows)]      # Creating 2D array for the 6x7 board

        
    
    def display(self):
         
        for s in self.grid:
            print ("|" + "|".join(s) + "|")
        



#testing
b = Board(6, 7, 4)
print (" ")
b.display()
print (" ")

        