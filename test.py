import random
import os
import time

class cell:
    def __init__(self, alive=False):
        self.alive = alive
    def birth(self):
        self.alive = True
    def kill(self):
        self.alive = False
    def is_alive(self):
        return self.alive

def test_cell():
    c = cell()
    assert not c.is_alive()
    c.birth()
    assert c.is_alive()
    c.kill()
    assert not c.is_alive()
    
test_cell()

class board:
    def __init__(self, N=40):
        self.N = N
        self.cells = [[cell() for i in range(N)] for j in range (N)]
    def randomize(self):
        for r in self.cells:
            for c in r:
                if random.randint(0,10) == 1:
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
        if r < 0: r = (self.N+r)%self.N
        if c < 0: c = (self.N+c)%self.N
        return (r,c)
    def count_neighbours(self, r, c):
        delta = (1,-1)
        count = 0
        for d in delta:
            wrapped = self.get_wrapped_coord(r+d,c)
            if self.cells[wrapped[0]][wrapped[1]].is_alive():
                count += 1
            wrapped = self.get_wrapped_coord(r,c+d)
            if self.cells[wrapped[0]][wrapped[1]].is_alive():
                count += 1
            wrapped = self.get_wrapped_coord(r+d,c+d)
            if self.cells[wrapped[0]][wrapped[1]].is_alive():
                count += 1
            wrapped = self.get_wrapped_coord(r+d,c-d)
            if self.cells[wrapped[0]][wrapped[1]].is_alive():
                count += 1
        return count
    def get_N(self):
        return self.N
    def quick_print(self):
        for r in range(self.N):
            for c in range(self.N):
                if self.is_alive(r,c):
                    print('#',end='')
                else:
                    print(' ',end='')
            print()
        print('-'*self.N)

def test_board():
    b = board(3)
    assert b.get_wrapped_coord(3,3) == (0,0)
    assert b.get_wrapped_coord(-1,0) == (2,0)
    assert b.get_wrapped_coord(-1,-1) == (2,2)
    b.birth_cell(1,1)
    assert b.count_neighbours(0,0) == 1
    b.birth_cell(0,0)
    assert b.count_neighbours(0,0) == 1
    b.birth_cell(1,0)
    assert b.count_neighbours(0,0) == 2
    
test_board()

class life:
    def __init__(self):
        self.board = board()
        self.N = self.board.N
        self.board.randomize()
    def iterate(self):
        newboard = board()
        for r in range(self.N):
            for c in range(self.N):
                neighbours = self.board.count_neighbours(r,c)
                if neighbours >= 2 and neighbours <= 3:
                    if self.board.is_alive(r,c):
                        newboard.birth_cell(r,c)
                if neighbours == 3:
                    newboard.birth_cell(r,c)
        self.board = newboard
        newboard.quick_print()

l = life()
while True:
    os.system("clear")
    l.iterate()
    time.sleep(1)