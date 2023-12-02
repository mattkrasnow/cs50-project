import pygame

class Enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.xaccel = 0.075
        self.jumping = False
        self.yaccel = 0.3
        self.yvel = 0

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
            if self.x < 800 - self.w:
                self.vel += self.xaccel
        else:
            self.dir = 'l'
            if self.x > 10:
                self.vel -= self.xaccel

        if self.jumping == False:
            self.vel *= 0.95
        self.x += self.vel
        if self.x <= 0:
            self.x = 0
            self.vel = 0
        if self.x >= 800 - self.w:
            self.x = 800 - self.w
            self.vel = 0
        if self.jumping == True:
            self.yvel -= self.yaccel
            self.y -= self.yvel    