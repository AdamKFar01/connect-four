import unittest
import sys
sys.path.insert(0, '.')
from src.board import Board

class TestBoard(unittest.TestCase):
    ##pass

    #testing rows
    def test_drop_token_correct_row(self):
        b = Board(6, 7, 4)
        row = b.drop_token(0, 'R')
        self.assertEqual(row, 5)

    #testing invalid columns
    def test_drop_token_invalid_column(self):
        b = Board(6, 7, 4)
        self.assertRaises(ValueError, b.drop_token, -1, 'R')

    #testing full columns
    def test_drop_token_full_column(self):
        b = Board(2, 7, 4)
        b.drop_token(0, 'R')
        b.drop_token(0, 'R')
        self.assertRaises(ValueError, b.drop_token, 0, 'R')

    #testing horizontal win
    def test_check_win_horizontal(self):
        b = Board(6, 7, 4)
        b.drop_token(0, 'R')
        b.drop_token(1, 'R')
        b.drop_token(2, 'R')
        b.drop_token(3, 'R')
        self.assertTrue(b.check_win(5, 3, 'R'))

    #testing vertical win
    def test_check_win_vertical(self):
        b = Board(6, 7, 4)
        b.drop_token(0, 'R')
        b.drop_token(0, 'R')
        b.drop_token(0, 'R')
        b.drop_token(0, 'R')
        self.assertTrue(b.check_win(2, 0, 'R'))

    #testing diagonal win
    def test_check_win_diagonal(self):
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
        self.assertTrue(b.check_win(2, 3, 'R'))

    #testing no win
    def test_check_win_no_win(self):
        b = Board(6, 7, 4)
        b.drop_token(0, 'R')
        b.drop_token(1, 'Y')
        self.assertFalse(b.check_win(5, 1, 'Y'))

    #testing draw
    def test_check_draw(self):
        b = Board(2, 2, 4)
        b.drop_token(0, 'R')
        b.drop_token(0, 'R')
        b.drop_token(1, 'R')
        b.drop_token(1, 'R')
        self.assertTrue(b.check_draw())


if __name__ == '__main__':
    unittest.main()