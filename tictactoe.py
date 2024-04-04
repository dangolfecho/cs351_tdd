class TicTacToe:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
            return True
        else:
            return False

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                return self.board[row][0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][2]
        return None

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

def play_game():
    game = TicTacToe()
    while True:
        game.print_board()
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if game.make_move(row, col):
            winner = game.check_winner()
            if winner:
                game.print_board()
                print(f"Player {winner} wins!")
                break
            elif game.is_board_full():
                game.print_board()
                print("It's a tie!")
                break
        else:
            print("Invalid move! Try again.")


if __name__ == "__main__":
    play_game()
