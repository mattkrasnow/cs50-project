import pygame
from hpbar import HPBar

class Enemy(object):
    def __init__(self, x, y, screenwidth, screenheight):
        self.x = x
        self.y = y
        self.vel = 0
        self.xaccel = 0.06
        self.jumping = False
        self.yaccel = 0.3
        self.yvel = 0
        self.hp = 6
        self.maxHp = 6
        self.hpBar = HPBar(6)

        beaverImg = pygame.image.load("beaversprite.png").convert_alpha()
        self.imgL = pygame.transform.scale_by(beaverImg, 0.3)
        self.imgR = self.imgL.copy()
        self.imgR = pygame.transform.flip(self.imgR, flip_x=True, flip_y=False)
        self.h = self.imgR.get_height()
        self.w = self.imgR.get_width()
        self.dir = 'r'
        self.screenwidth = screenwidth
        self.screenheight = screenheight

    def display(self, win):
        if self.dir == 'r':
            win.blit(self.imgR, (self.x, self.y))
        else:
            win.blit(self.imgL, (self.x, self.y))
        self.hpBar.hp = self.hp
        self.hpBar.display(win, self.x + self.w/2, self.y - 30)
    
    def move(self, duck):
        if self.y >= self.screenheight - self.h:
            self.y = self.screenheight - self.h
            self.jumping = False
        if duck.x + duck.w/2 > self.x + self.w/2:
            self.dir = 'r'
            if self.x < self.screenwidth - self.w:
                self.vel += self.xaccel
        else:
            self.dir = 'l'
            if self.x > 10:
                self.vel -= self.xaccel
        if duck.y + duck.h < self.y + self.h and self.jumping == False:
            self.jumping = True
            self.yvel = 10
        if self.jumping == True:
            self.yvel -= self.yaccel
            self.y -= self.yvel  
        

        if self.jumping == False:
            self.vel *= 0.95
        self.x += self.vel
        if self.x <= 0:
            self.x = 0
            self.vel = 0
        if self.x >= self.screenwidth - self.w:
            self.x = self.screenwidth - self.w
            self.vel = 0
        
    def duckCollision(self, duck):
        if duck.w + duck.x > self.x and duck.x < self.x + self.w and duck.y + duck.h > self.y and duck.y < self.y + self.h:
            return True
        return False