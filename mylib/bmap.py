import random

sur = [(-1,-1), (-1,0), (-1,+1), (0,-1), (0,1),(1,-1), (1,0), (1,1)]
class Bmap:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mmap = [[0 for _ in range(y+2)] for _ in range(x+2)]
        self.mmap[0] = [-1] * len(self.mmap[0])
        self.mmap[self.x + 1] = [-1] * len(self.mmap[self.x + 1])
        for column in [0,self.y + 1]:
            for row in self.mmap:
                row[column] = -1       
 
    def set_bomb(self, n):
        for _ in range(n):
            while True:
                bx, by = random.randint(1, self.x), random.randint(1, self.y)
                if self.mmap[bx][by] != 9:
                    break
            self.mmap[bx][by] = 9
 
    def extract_bombMap(self):
        for r in range(1,self.x + 1):
            for c in range(1, self.y +1):
                v = 0
                for t in sur:
                    v += 1 if self.mmap[t[0] + r][t[1] + c] == 9 else 0
                self.mmap[r][c] = v if self.mmap[r][c] != 9 else 9

    def get_bomb_status(self, x, y):
        return self.mmap[x][y]
