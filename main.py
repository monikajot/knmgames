import numpy as np

class Game:

    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k
        self.utility = 0


    def initialize_game(self):
        self.current_state = np.full((self.m, self.n), "_", dtype=object)
        self.o = []
        self.x = []
        return self.current_state

    def drawboard(self):
        print(self.current_state)

    def is_valid(self, coord):
        x,y = coord[0], coord[1]

        if self.current_state((x, y)) != '_':  # empty (write this when we have the board)
            return False
        if (x >= self.n) or ( x < 0) or (y >= self.m) or (y < 0):
            return False
        return True

    def is_terminal(self):
        # check horizontaly and vertically
        Max_win = 'X' * self.k
        Min_win = 'O' * self.k
        for j in range(2):
            if j == 1:
                self.current_state.T
            for i in range(self.m):
                l = self.current_state[i].tolist()

                final = "".join(self.current_state[i])

                if Max_win in final:
                    self.utility += 1
                    return True
                elif Min_win in final:
                    self.utility = -1
                    return True
        a = self.current_state
        diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
        for j in range(2):
            if j == 1:
                diags = [a[::, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
            for i, elem in enumerate(diags):
                l = self.current_state.tolist()
                final = "".join(self.diags[i])
                if Max_win in final:
                    self.utility +=1
                    return True
                elif Min_win in final:
                    self.utility -= 1
                    return True

        for i in range(self.m):
            for j in range(self.n):
                if self.current_state[i][j] == '-':
                    return False
        return False

    """def MINIMAX_DECISION(self, state):
        # returns an action
        return #argmax a

        ACTIONS(state)
        MIN - VALUE(RESULT(state, a))"""

    def MAX_VALUE(self, state):
        # returns utility value
        if self.is_terminal():
            return self.utility
        v = -float(inf)
        best_action = 0,0
        for j in self.m:
            for i in self.n:

                if self.current_state[j, i] = '_':
                    self.current_state[j,i] = 'X'
                    MIN_VALUE(self.current_state, )

                if  v <  MIN_VALUE(RESULT(state, a):
                    best_action = i,j
        return v

    def MIN_VALUE(self, state):
        # returns utility value
        if TERMINAL - TEST(state):
            return UTILITY(state)
        v = math.inf
        for a in ACTIONS(state):
            v = MIN(v, MAX - VALUE(RESULT(state, a))
        return v



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game(3, 3, 3)
    game.initialize_game()
    game.drawboard()
    game.current_state = np.zeros((3,3))+np.diagonal()
    print(game.is_terminal())


