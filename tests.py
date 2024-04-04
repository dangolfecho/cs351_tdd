import unittest
from tictactoe import TicTacToe

class Tests(unittest.TestCase):
    def test_first(self):
        game = TicTacToe()
        expected_board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(expected_board, game.board)
    
    def test_make_move_valid(self):
        game = TicTacToe()
        self.assertTrue(game.make_move(0, 0))
        self.assertEqual(game.board[0][0], 'X')
        
    def test_make_move_invalid(self):
        game = TicTacToe()
        game.make_move(0, 0)
        self.assertFalse(game.make_move(0, 0))  # Trying to make a move on an already occupied cell

    def test_check_winner_row(self):
        game = TicTacToe()
        game.board = [
            ['X', 'X', 'X'],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(game.check_winner(), 'X')

    def test_check_winner_column(self):
        game = TicTacToe()
        game.board = [
            ['X', ' ', ' '],
            ['X', ' ', ' '],
            ['X', ' ', ' ']
        ]
        self.assertEqual(game.check_winner(), 'X')
    
    def test_check_winner_diagonal(self):
        game = TicTacToe()
        game.board = [
            ['X', ' ', ' '],
            ['X', ' ', ' '],
            [' ', ' ', 'X']
        ]
        self.assertEqual(game.check_winner(), 'X')

if __name__ == '__main__':
    unittest.main()
