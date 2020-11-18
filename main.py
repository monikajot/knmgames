import numpy as np
import math


class Game:

    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k
        self.utility = 0
        self.initialize_game()
        #This indicates what player starts the game. Right now is Max
        self.turn = 'X'

    def initialize_game(self):
        self.current_state = np.full((self.m, self.n), "_", dtype=object)

    def drawboard(self):
        print(self.current_state)

    def is_valid(self, coord):
        x, y = coord[0], coord[1]
        #check is the chosen cell is empty, if it's not return False (not valid)
        if self.current_state[x][y] != '_':
            return False
        #check if the cell is within the dimensions of the board, if it's not, return False
        if (x >= self.n) or (x < 0) or (y >= self.m) or (y < 0):
            return False
        return True

    def is_terminal(self):
        #check if there is a win horizontally or vertically
        Max_win = 'X' * self.k
        Min_win = 'o' * self.k
        for j in range(2):
            board = self.current_state
            if j == 1:
                #Transpose the board, so you can check vertically, but using the same method as horizontally
                board = self.current_state.T
            #for i in range(self.m):
            for i in range(board.shape[0]):
                l = board[i].tolist()
                final = "".join(l)
                #if Max or Min win, update the utility of the game to 1/-1/0 and return True
                if Max_win in final:
                    self.utility = 1
                    return True
                elif Min_win in final:
                    self.utility = -1
                    return True
        #check the diagonals
        a = self.current_state
        diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
        for j in range(2):
            if j == 1:
                diags = [a[::, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
            for i, elem in enumerate(diags):
                #l = self.current_state.tolist()
                final = "".join(diags[i])
                if Max_win in final:
                    self.utility = 1
                    return True
                elif Min_win in final:
                    self.utility = -1
                    return True
        #check if there is a tie
        tie = True
        for i in range(self.m):
            for j in range(self.n):
                if self.current_state[i][j] == '_':
                    tie = False
        #if there is a tie, set the utility of the game to 0 and return True
        if tie:
            self.utility = 0
            return True
        return False


    def MAX_VALUE(self):
        #check if the game is over, and return the utility in that case
        end = self.is_terminal()
        if end:
            return self.utility, 0, 0
        #set v to -infinity
        v = -float('inf')
        best_x = 0
        best_y = 0
        #check what coordinates are blank in the current state. Each blank coordinate will be a node in our tree
        for j in range(self.m):
            for i in range(self.n):
                if self.current_state[j][i] == '_':
                    #set the blank coordinate to 'X' and get the utility value of having (j,i) as the next move
                    #by calling MIN_VALUE
                    self.current_state[j][i] = 'X'
                    minv, minx, miny = self.MIN_VALUE()
                    #if the minv is greater than our current v, set v to minv and your best action to j, i
                    if v < minv:
                        v = minv
                        best_x = j
                        best_y = i
                     #set the current_state back to '_' since we haven't yet made a move
                    self.current_state[j][i] = '_'
        return v, best_x, best_y

    def MIN_VALUE(self):
        #check if the game is over, and return the utility in that case
        end = self.is_terminal()
        if end:
            return self.utility, 0, 0
        v = float('inf')
        best_x = 0
        best_y = 0
        for j in range(self.m):
            for i in range(self.n):
                if self.current_state[j][i] == '_':
                    self.current_state[j][i] = 'o'
                    maxv, maxx, maxy = self.MAX_VALUE()
                    #if the maxv is smaller than our current v, set v to maxv and your best action to j, i
                    if v > maxv:
                        v = maxv
                        best_x = j
                        best_y = i
                    self.current_state[j][i] = '_'
        return v, best_x, best_y

    def play(self):
        game_over = False
        while not game_over:
            #check if the game is done, and if it is print the board and type who wins
            if self.is_terminal():
                if self.utility == 1:
                    print(self.drawboard())
                    print("Max wins the game")
                    game_over = True
                elif self.utility == -1:
                    print(self.drawboard())
                    print("Min wins the game")
                    game_over = True
                elif self.utility == 0:
                    print(self.drawboard())
                    print("There is a tie, no one wins")
                    game_over = True
            else:
                print(self.current_state)
                #when it's Max's turn
                if self.turn == 'X':
                    #get our recommendations for Max, and ask Max (the player) to input its move
                    v, v_x, v_y = self.MAX_VALUE()
                    print("Max, our recommendation is x = " + str(v_x) +" and y = " + str(v_y))
                    #Check if the inputted entries are valid, if it's not, ask again
                    valid = False
                    while not valid:
                        x = int(input("Please enter your choice for coordinate x = "))
                        y = int(input("Please enter your choice for coordinate y = "))
                        if self.is_valid((x, y)):
                            self.current_state[x][y] = 'X'
                            #change the turn to Min
                            self.turn = 'o'
                            valid = True
                        else:
                            print("Your chosen coordinates are not valid. Please try again")
                #When it's Min's turn, get the optimal coordinates and play those coordinates
                else:
                    v, v_x, v_y = self.MIN_VALUE()
                    self.current_state[v_x][v_y] = 'o'
                    self.turn = 'X'



if __name__ == '__main__':
    game = Game(3, 3, 3)
    game.play()



