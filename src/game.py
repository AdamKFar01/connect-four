import logging 
logging.basicConfig(filename = 'game.log', level = logging.INFO, format = '%(asctime)s - %(message)s')


class Game:


    def __init__(self, board, Player1, Player2):
        self.board = board
        self.Player1 = Player1
        self.Player2 = Player2

        self.current_player = Player1

    def play_turn(self):
        # Starting the game by asking the first player to play their turn
        #column = int(input(f"{self.current_player.name}, choose a column: "))
        
        # calls the row and token of the player who played their turn in "column" 
        #row = self.board.drop_token(column, self.current_player.token)

        # added a try/except while loop so that the game does not end straight when a player inputs a wrong input (e.g. out of board size/range)
        while True:
        
            try: 
                column = int(input(f"{self.current_player.name}, choose a column: "))
                row = self.board.drop_token(column, self.current_player.token)
                
                # player move logging
                logging.info(f"{self.current_player.name} dropped a token in row {row} and column {column}")
                break
            
            # if an errors occurs, print:
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

                # error logging
                logging.warning(f"Invalid input: {e} !")


        # if a player won (called from board.py/check_win()), it outputs the player who won 
        if self.board.check_win(row, column, self.current_player.token):
            print (f"{self.current_player.name} won!")

            # win logging 
            logging.info(f"{self.current_player.name} won the game !")

            print (" ")
            self.board.display()
            print (" ")
            return True

        # if it was a draw (called from board.py/check_draw()), it outputs a message announcing the draw
        if self.board.check_draw():
            print (f"It's a draw! ")

            # draw logging 
            logging.info("This game ended with a draw... Maybe next time! ")

            print (" ")
            self.board.display()
            print (" ")
            return True


        # if none of the two statements above were met, meaning the game is not yet over, switch players to play their turns with a ternary operator
        self.current_player = self.Player2 if self.current_player == self.Player1 else self.Player1
        
        return False


    def run(self):
        # display the board for the game
        print (" ")
        print (" ")
        print (" ")
        self.board.display()
        print (" ")

        # game start logging
        logging.info(f"The game has started! Good luck! ")

        while not self.play_turn():
            
            # displays the board one last time with the final results once a player won or a draw was met 
            print (" ")
            print (" ")
            print (" ")
            self.board.display()
            print (" ")