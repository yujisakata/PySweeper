import pygame
class TileImage:
    def __init__(self):
        self.img_smile = pygame.image.load("img/Smile.png")
        self.img_wall = pygame.image.load("img/Wall.png")
        self.img_init = pygame.image.load("img/Init.png")
        self.img_flag = pygame.image.load("img/Flag.png")
        self.img_wrong_flag = pygame.image.load("img/WrongFlag.png")
        self.img_question = pygame.image.load("img/Question.png")
        self.img_opened = [pygame.image.load(f"img/Opened_{str(i)}.png") for i in range(0,10)]
        self.img_header = pygame.image.load("img/Header.png")
        self.img_wrong_flag

    def get_image(self, b, v, game_status):
        images = {
            -2: self.img_smile,
            -1: self.img_wall,
            0: self.img_init,
            1: self.img_flag,
            2: self.img_opened[b],
            3: self.img_question,
            4: self.img_wrong_flag
        }
        return images.get(v, self.img_question) 
    
    def get_header_image(self):
        return self.img_header

