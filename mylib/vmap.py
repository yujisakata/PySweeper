# init = 0, flag =1, opened = 2, question = 3, wall = -1, smile = -2

NXT = (1,3,2,0)

class Vmap:
    def __init__(self, x, y, n):
        self.x, self.y, self.bn  = (x, y, n)
        self.mmap = [[0 for _ in range(self.y+2)] for _ in range(self.x+2)]
        self.to_be_opened = self.x * self.y - self.bn
        self.n_flag = n
        self.create_wall(-1)

    def set_opened(self, x, y):
        self.to_be_opened -= 1
        self.mmap[x][y] = 2

    def open_all(self):
        self.mmap = [[2 for _ in range(0,self.y+2)] for _ in range(0,self.x+2)]
        self.create_wall(-1)

    def set_next_status(self, x, y):
        self.n_flag += 1 if self.mmap[x][y] == 1 else 0
        self.mmap[x][y] = NXT[self.mmap[x][y]]
        self.n_flag -= 1 if self.mmap[x][y] == 1 else 0

    def get_status(self, x, y):
        return self.mmap[x][y]
    
    def get_n_flag(self):
        return self.n_flag

    def is_opened_all(self):
        return self.to_be_opened == 0
    
    def is_finished(self):
        return self.is_opened_all() and (self.get_n_flag() == 0)

    def set_success_status(self):
        self.create_wall(-2)
    
    def create_wall(self,k):
        self.mmap[0] = [k] * len(self.mmap[0])
        self.mmap[self.x + 1] = [k] * len(self.mmap[self.x + 1])
        for column in [0,self.y + 1]:
            for row in self.mmap:
                row[column] = k
