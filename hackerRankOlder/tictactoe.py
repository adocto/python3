# game
# initialize game: >>COMPLETE
#     - set or reset board to empty board
#     - print board

# print board: >>COMPLETE
#     - print status of board

# prompt player for input: >>COMPLETE
#     - set of coordinates
#     - if validate move is true:
#         - set on board (place player marker on spot on board)
#         - decrement moves remaining
#     - else:
#         - notify user
#         - reprompt for move
#

# check win condition: >>COMPLETE
#     - check for win
#     - set appropriate boolean
#     - set winner

# validate move: >>COMPLETE
#     - check if out of bounds of array
#     - check if spot is taken
#     - return true or false


# play game(): >>COMPLETE
#    - while win condition is false or move_rem == 0:
#      - prompt player for input >>COMPLETE
#      - print board >>COMPLETE
#      - check win condition
#      - switch player >>COMPLETE

#    if win condition = true - print self.winner wins!
#    else it's a tie


import numpy as np


class Game:

    def __init__(self):
        self.board = [[None for i in range(3)] for j in range(3)]
        self.player = 0
        self.win = False
        self.moves_remaining = 9
        self.winner = -1

    def resetBoard(self):
        self.board = [[None for i in range(3)] for j in range(3)]

    def playGame(self):

        # prompt player for turns until someone wins or game is tied
        while (not self.win) and self.moves_remaining > 0:
            self.print_board()
            self.prompt_input()
            self.check_win()
            self.switch_player()

        # check and report winner or tie
        if self.win:
            print("Player %d wins!" % self.winner)
        else:
            print("It's a tie!")

    # switch players after turn
    def switch_player(self):
        if self.player == 0:
            self.player = 1
        else:
            self.player = 0

    def check_win(self):
        # check each row for win condition
        for row in self.board:
            if row.count(0) == 3:
                self.winner = 0
                self.win = True
                return
            elif row.count(1) == 3:
                self.winner = 1
                self.win = True
                return

        # convert to numpy array to transpose
        temp_board = np.array(self.board)
        temp_board = temp_board.transpose()

        # iterating through the rows
        for col in temp_board:
            if np.count_nonzero(col == 0) == 3:
                self.winner = 0
                self.win = True
                return
            elif np.count_nonzero(col == 1) == 3:
                self.winner = 1
                self.win = True
                return

        # check for win condition in main diagonal
        main_diagonal = [self.board[i][i] for i in range(len(self.board))]
        if main_diagonal.count(0) == 3:
            self.winner = 0
            self.win = True
            return
        elif main_diagonal.count(1) == 3:
            self.winner = 0
            self.win = True
            return

        # check for win condition in alt diagonal
        alt_diagonal = [self.board[i][len(self.board) - 1 - i] for i in range(len(self.board))]
        if alt_diagonal.count(0) == 3:
            self.winner = 0
            self.win = True
            return
        elif alt_diagonal.count(0) == 3:
            self.winner = 0
            self.win = True
            return

    def print_board(self):
        for i in self.board:
            print(", ".join([str(l).rjust(2) for l in i]))

    def prompt_input(self):
        # prompt player for input
        x = int(input("Player %d enter row: " % self.player))
        y = int(input("Player %d enter column: " % self.player))
        # keep reprompting until move is valid
        while not self.validate_move((x, y)):
            x = int(input("Player %d enter row: " % self.player))
            y = int(input("Player %d enter column: " % self.player))
        # set move on board
        self.board[x][y] = self.player
        self.moves_remaining -= 1

    def validate_move(self, move):
        # move is a tuple of x and y coordinates
        valid_input = False  # valid input flag
        empty_space = False  # valid empty space flag
        # are inputs from player within bounds of array?
        while valid_input == False and empty_space == False:
            for int in move:
                if (0 <= int) and (2 >= int):
                    valid_input = True
                else:
                    print("You entered an invalid coordinate")
                    return False
            # check if value at tupple index == None:
            if self.board[move[0]][move[1]] == None:
                empty_space = True
            else:
                print("That space is taken")
                return False
        return True
        pass


if __name__ == "__main__":
    game = Game()
    game.playGame()
