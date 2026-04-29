from src.board import Board
from src.player import Player
from src.game import Game

# linking user input to 
rows = int(input("Please enter the number of rows: "))

columns = int(input("Please enter the number of columns: "))

win_len = int(input("Please enter the number of tokens required for a win: "))

if win_len > rows or win_len > columns:
    print ("Win length is too large for the board. Please restart the game.")
    exit()


b = Board(rows, columns, win_len)

Player1 = Player("White", "W")
Player2 = Player("Black", "B")

game = Game(b, Player1, Player2)

game.run()

