import numpy as np

class Game:

    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k

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
                l = self.current_state.tolist()
                final = "".join(self.current_state[i])

                if Max_win in final:
                    return "Max wins"
                elif Min_win in final:
                    return "Min wins"

        diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
        for j in range(2):
            if j == 1:
                diags = [a[::, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
            for i, elem in enumerate(diags):
                l = self.current_state.tolist()
                final = "".join(self.diags[i])
                if Max_win in final:
                    return "Max wins"
                elif Min_win in final:
                    return "Min wins"



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
