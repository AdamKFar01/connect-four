
class Game:


    def __init__(self, board, Player1, Player2):
        self.board = board
        self.Player1 = Player1
        self.Player2 = Player2

        self.current_player = Player1

    def play_turn(self):
        # Starting the game by asking the first player to play their turn
        column = int(input(f"{self.current_player.name}, choose a column: "))
        
        # calls the row and token of the player who played their turn in "column" 
        row = self.board.drop_token(column, self.current_player.token)

        # if a player won (called from board.py/check_win()), it outputs the player who won 
        if self.board.check_win(row, column, self.current_player.token):
            print (f"{self.current_player.name} won!")
            return True

        # if it was a draw (called from board.py/check_draw()), it outputs a message announcing the draw
        if self.board.check_draw():
            print (f"It's a draw! ")
            return True

        # if none of the two statements above were met, meaning the game is not yet over, switch players to play their turns with a ternary operator
        self.current_player = self.Player2 if self.current_player == self.Player1 else self.Player1
        
        return False


    def run(self):
        # display the board for the game
        self.board.display()
        
        
        while not self.play_turn():
            
            # displays the board one last time with the final results once a player won or a draw was met 
            self.board.display()