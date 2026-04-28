

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



    def check_win(self, row, column, token):

        # HORIZONTAL WIN DETECTION                                                                  
        count_consecutives = 0                                                      # To get a win, 4 consecutive tokens are needed
        for c in range (column -1, -1, -1):                                         # Looping from last column to first column (right to left)
            if self.grid[row][c] == token:
                count_consecutives += 1                                         
            else: break                       

        for c in range (column +1, self.columns):                                   # Looping from first column to last column
            if self.grid[row][c] == token:
                count_consecutives += 1
            else: break

        if count_consecutives +1 >= self.win_len: return True                       # If the number of tokens needed to win are met, return True

        # VERTICAL WIN DETECTION
        count_consecutives = 0                                                      # Resetting count_consecutives to 0
        for r in range (row -1, -1, -1):                                            # Looping from last row to first row (down to up)
            if self.grid[r][column] == token:
                count_consecutives += 1                                         
            else: break                       

        for r in range (row +1, self.rows):                                         # Looping from first row to last row
            if self.grid[r][column] == token:
                count_consecutives += 1
            else: break

        if count_consecutives +1 >= self.win_len: return True  


        # DIAGONAL WIN DETECTION: 
        count_consecutives = 0
        # Bot right to Top left
        r, c = (row - 1, column - 1)
        while r >= 0 and c >= 0:
            if self.grid[r][c] == token:
                count_consecutives += 1
                r -= 1
                c -= 1
            else: break
    
        # Top left to Bot right
        r, c = (row + 1, column + 1)
        while r < self.rows and c < self.columns:
            if self.grid[r][c] == token:
                count_consecutives += 1
                r += 1
                c += 1
            else: break      
        if count_consecutives +1 >= self.win_len: return True  
        

        count_consecutives = 0
        # Bot left to Top right
        r, c = (row - 1, column + 1)
        while r >= 0 and c < self.columns:
            if self.grid[r][c] == token:
                count_consecutives += 1
                r -= 1
                c += 1
            else: break
        
        # Top right to Bot left
        r, c = (row + 1, column - 1)
        while r < self.rows and c >= 0:
            if self.grid[r][c] == token:
                count_consecutives += 1
                r += 1
                c -= 1
            else: break
        if count_consecutives +1 >= self.win_len: return True  

        return False  

# Testing

b = Board(6, 7, 4)
b.drop_token(0, 'R')
b.drop_token(1, 'Y')
b.drop_token(1, 'R')
b.drop_token(2, 'Y')
b.drop_token(2, 'Y')
b.drop_token(2, 'R')
b.drop_token(3, 'Y')
b.drop_token(3, 'Y')
b.drop_token(3, 'Y')
b.drop_token(3, 'R')
print(b.check_win(2, 3, 'R'))

print (" ")
b.display()
print (" ")

