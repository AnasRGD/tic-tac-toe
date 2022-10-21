import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use a single list to represent 3x3 board
        self.current_winner = None # To keep track of the winner
    
    def print_board(self):
        #This is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print ('| '+ ' | '.join(row) + ' |' )

    @staticmethod    
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print ('| '+ ' | '.join(row) + ' |' )
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row, column or diagonal, let's check 'em all
        # 
        # first let's check the row :
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3 ]
        if all(spot == letter for spot in row):
            return True
        
        # first let's check the colomn :
        col_ind = square % 3
        col = [self.board[col_ind+(3*i)] for i in range(3)]
        if all(spot == letter for spot in col):
            return True

        # check the diagonals
        # but only if the square is an even number [0,2,4,6,8]
        # these are the only moves to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):
    # returns the winner's letter of the game ! or None for tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' #Starting letter
    
    # Iterate the game while it has an empty squares
    while game.empty_squares():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}.')
                game.print_board()
                print('') # Empty line for clear display :) 

            if game.current_winner:
                if print_game:
                    print (letter + ' won !')
                return letter

            # Alternate letter after playing the move
            letter = 'O' if letter == 'X' else 'X'  # switches player
        time.sleep(1)
    if print_game:
        print('It\'s a tie !')


if __name__=='__main__':
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)