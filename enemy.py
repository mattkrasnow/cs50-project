import pygame

class Enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        beaverImg = pygame.image.load("beaversprite.png").convert_alpha()
        self.imgL = pygame.transform.scale_by(beaverImg, 0.5)
        self.imgR = self.imgL.copy()
        self.imgR = pygame.transform.flip(self.imgR, flip_x=True, flip_y=False)
        self.h = self.imgR.get_height()
        self.w = self.imgR.get_width()
        self.dir = 'r'

    def display(self, win):
        if self.dir == 'r':
            win.blit(self.imgR, (self.x, self.y))
        else:
            win.blit(self.imgL, (self.x, self.y))
    
    def move(self, duck):
        if duck.x + duck.w/2 > self.x + self.w/2:
            self.dir = 'r'
        else:
            self.dir = 'l'