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

if __name__ == '__main__':
    unittest.main()