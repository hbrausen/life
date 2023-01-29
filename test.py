import random

class cell:
    def __init__(self, alive=False):
        self.alive = alive
    def birth(self):
        self.alive = True
    def kill(self):
        self.alive = False
    def is_alive(self):
        return self.alive

class board:
    def __init__(self, N=20):
        self.N = N
        self.cells = [[cell() for i in range(N)] for j in range (N)]
    def randomize(self):
        for r in self.cells:
            for c in r:
                if random.randint(0,3) == 1:
                   c.birth()
                else:
                    c.kill()
    def birth_cell(self, r, c):
        self.cells[r][c].birth()
    def kill_cell(self, r, c):
        self.cells[r][c].kill()
    def is_alive(self, r, c):
        return self.cells[r][c].is_alive()
    def get_wrapped_coord(self, r, c):
        if r >= self.N: r %= self.N
        if c >= self.N: c %= self.N
        if r < 0: r = (self.N-r)%self.N
        if c < 0: c = (self.N-c)%self.N
        return (r,c)
    def count_neighbours(self, r, c):
        delta = (1,0,-1)
        count = -2
        for d in delta:
            wrapped = self.get_wrapped_coord(r+d,c)
            if self.cells[wrapped[0]][wrapped[1]].is_alive():
                count += 1
            wrapped = self.get_wrapped_coord(r,c+d)
            if self.cells[wrapped[0]][wrapped[1]].is_alive():
                count += 1
        return count
    def get_N(self):
        return self.N
    def clone(self):
        new_board=board()
        for r in range(self.N):
            for c in range(self.N):
                if self.is_alive(r,c):
                    new_board.birth_cell(r,c)
        return new_board
    def quick_print(self):
        for r in range(self.N):
            for c in range(self.N):
                if self.is_alive(r,c):
                    print('#',end='')
                else:
                    print(' ',end='')
            print()
        print('-'*self.N)

class life:
    def __init__(self):
        self.board = board()
        self.N = self.board.N
        self.board.randomize()
    def iterate(self):
        newboard = self.board.clone()
        for r in range(self.N):
            for c in range(self.N):
                neighbours = self.board.count_neighbours(r,c)
                if neighbours >= 2 and neighbours <= 3:
                    newboard.birth_cell(r,c)
                else:
                    newboard.kill_cell(r,c)
        self.board = newboard
        newboard.quick_print()

l = life()
l.iterate()
l.iterate()
l.iterate()