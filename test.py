import random
import time
import os

from rich.live import Live
from rich.table import Table
from rich.panel import Panel

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
    def __init__(self, N=40):
        self.N = N
        self.cells = [[cell() for i in range(N)] for j in range (N)]
    def randomize(self):
        for r in self.cells:
            for c in r:
                if random.randint(0,1) == 1:
                   c.birth()
                else:
                    c.kill()
    def birth_cell(self, r, c):
        self.cells[r][c].birth()
    def kill_cell(self, r, c):
        self.cells[r][c].kill()
    def get_wrapped_coord(self, r, c):
        if r > self.N: r %= self.N
        if c > self.N: c %= self.N
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
        new_board=self.__init__()
        for r in self.cells:
            for c in r:
                if c.is_alive():
                    new_board[r][c].birth()
        return new_board

class life:
    def __init__(self):
        self.board = board()
        self.N = self.board.N
    def iterate(self):
        newboard = self.board.clone()
        for r in range(self.N):
            for c in range(self.N):
                neighbours = self.board.count_neighbours(r,c)
                if neighbours >= 2 and neighbours <= 3:
                    newboard.birth_cell(r,c)
                else:
                    newboard.kill_cell(r,c)
        self = newboard

