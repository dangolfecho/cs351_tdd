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

if __name__ == '__main__':
    unittest.main()