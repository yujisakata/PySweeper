import sys
import tkinter as tk
import pygame
from mylib.bmap import Bmap
from mylib.vmap import Vmap
from mylib.imgSelector import TileImage

TILE = 55
HEADER_HEIGHT = 28
SUR = [(-1,-1), (-1,0), (-1,+1), (0,-1), (0,1),(1,-1), (1,0), (1,1)]
OPTIONS = ["Easy", "Medium", "Difficult", "Awesome"]
SIZE =[(9,9,9), (16,16,40), (30,16,99),(30,16,199)]
COLOR_LBLUE = (0, 192, 225)
FONT = ("BIZ UDPゴシック",12)

class Main:
    def main(self):

        self.select_mapsize()

        # Do mainlogic using pygame
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        screen = pygame.display.set_mode(((self.mx + 2)*TILE, (self.my + 2)*TILE+HEADER_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)
        self.start_time = 0
        self.finished_time = 0

        
        while True:
            for event in pygame.event.get():
                # event processing
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.MOUSEBUTTONDOWN and self.game_status == 0:
                    if (self.start_time == 0):
                        self.start_time = pygame.time.get_ticks()
                        print(f"Start = {self.start_time}")
                    px, py = (event.pos[0] // TILE, (event.pos[1]- HEADER_HEIGHT) // TILE)
                    if event.button == 1 and self.vmap.get_status(px, py) == 0:
                        self.vmap.set_opened(px, py)
                        if self.bmap.get_bomb_status(px, py) == 0:
                            self.recursive_open(px,py)
                        if self.bmap.get_bomb_status(px, py) == 9:
                            self.game_status = 1
                    if event.button == 3:
                        self.vmap.set_next_status(px,py)

                # detect game status change
                if self.game_status == 1:
                    if self.finished_time == 0:
                        self.finished_time = pygame.time.get_ticks()
                    self.vmap.open_all()
                    
                if self.vmap.is_finished():
                    self.game_status = 2
                    if self.finished_time == 0:
                        self.finished_time = pygame.time.get_ticks()
                    self.vmap.set_success_status()

            # refresh screen            
            for x in range(self.mx + 2 ):
                screen.blit(self.tm.get_header_image(), [x*TILE,0])
                for y in range(self. my + 2):
                    screen.blit(self.tm.get_image(self.bmap.get_bomb_status(x, y),self.vmap.get_status(x,y),self.game_status),[x*TILE, y*TILE+HEADER_HEIGHT])
            screen.blit(self.get_header_info() ,[(self.mx // 2) * TILE, 5])
            pygame.display.update()
            self.clock.tick(10)

    def select_mapsize(self):
        # Select mapsize using tkinter
        root = tk.Tk()
        root.title("Select map size")
        root.geometry("300x"+ str((len(SIZE)+1)*30))
        radios = [None] * len(SIZE)
        selected_value = tk.IntVar(value=0)
        for i, item in enumerate(OPTIONS):
            radios[i] = tk.Radiobutton(root, text=item + " "+ str(SIZE[i]), font = FONT,variable=selected_value, value=i)
            radios[i].pack(anchor=tk.W)
        button = tk.Button(root, text = "Select", font = FONT, command = lambda: self.show_selected(root, selected_value.get()))
        button.pack(anchor = tk.S)
        root.mainloop()            

    def show_selected(self,tk, v):
        self.game_init(v)
        tk.destroy()
    
    def game_init(self,v):
        self.mx, self.my, self.bn = SIZE[v]
        self.bmap, self.vmap = Bmap(self.mx, self.my), Vmap(self.mx, self.my,self.bn)
        self.game_status = 0
        self.bmap.set_bomb(self.bn)
        self.bmap.extract_bombMap()
        self.tm = TileImage()

    def recursive_open(self, x, y):
        for t in SUR:
            sx, sy =  x + t[0], y + t[1]
            if self.vmap.get_status(sx, sy) != 2 and self.vmap.get_status(sx, sy) != -1:
                self.vmap.set_opened(sx, sy)
                if self.bmap.get_bomb_status(sx, sy) == 0:
                    self.recursive_open(sx, sy)

    def get_header_info(self):
        current_time = 0 if self.start_time == 0 else self.finished_time if self.game_status != 0 else pygame.time.get_ticks() - self.start_time
                 
        txt = self.font.render("Bomb = {}, Time = {}".format(self.vmap.get_n_flag(),\
                                                              self.format_minutes_seconds(current_time // 1000)),True, COLOR_LBLUE)
        return txt
    
    def format_minutes_seconds(self, sec):
        min = sec // 60
        sec = sec % 60
        return f"{min:02}:{sec:02}"
        

if __name__ == '__main__':
    main = Main()
    main.main()
