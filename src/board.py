

class Board:


    def __init__(self, rows, columns, win_len):
        
        self.rows = rows                            # Assigning rows
        self.columns = columns                      # Assigning columns
        self.win_len = win_len                      # Assigning win_len

        self.grid = [[' ' for i in range (columns)] for j in range (rows)]      # Creating 2D array for the 6x7 board



  
    def display(self):
         
        for s in self.grid:
            print ("|" + "|".join(s) + "|")                                     # The two "|" before and after are the outer bars of the grid
        



    def drop_token(self, column, token):                                        # To place token in the lowest empty row for each column
        
        for i in range (self.rows -1, -1, -1):                                  # Looping from bottom row to top row (inverse loop, from end to beginning)
            
            if self.grid[i][column] == ' ':                                     # If statement to add a token to the lowest column that is empty 
                self.grid[i][column] = token

                break


# Testing

b = Board(6, 7, 4)
b.drop_token(3, 'R')
print (" ")
b.display()
print (" ")

        