import pygame
from hpbar import HPBar
import math

class Duck(object):
    def __init__(self, x, y, screenwidth, screenheight):
        self.x = x
        self.y = y
        self.vel = 0
        self.xaccel = 0.2
        self.jumping = False
        self.yaccel = 0.3
        self.yvel = 0
        self.dir = 'r'
        self.hp = 10
        self.maxHp = 10
        self.hpBar = HPBar(10)
        self.guntipX = self.x
        self.guntipY = self.y

        duckImg = pygame.image.load("cs50duck.png").convert_alpha()
        self.imgR = pygame.transform.scale_by(duckImg, 0.2)
        self.imgL = self.imgR.copy()
        self.imgL = pygame.transform.flip(self.imgL, flip_x=True, flip_y=False)
        self.h = self.imgR.get_height()
        self.w = self.imgR.get_width()
        self.screenwidth = screenwidth
        self.screenheight = screenheight

    def display(self, win):
        gunX = self.x + self.w/2
        gunY = self.y + 3*self.h/4
        if self.dir == 'r':
            win.blit(self.imgR, (self.x, self.y))
            gunX += 20
        else:
            win.blit(self.imgL, (self.x, self.y))
            gunX -= 20
        self.hpBar.hp = self.hp
        self.hpBar.display(win, self.x + self.w/2, self.y - 30)
        
        mouseX, mouseY = pygame.mouse.get_pos()
        xDiff = mouseX - gunX
        yDiff = mouseY - gunY
        normFactor = math.sqrt(xDiff * xDiff + yDiff * yDiff)
        xDiff = 20 * xDiff / normFactor
        yDiff = 20 * yDiff / normFactor
        for i in range(0, 50):
            pygame.draw.circle(win, (0, 0, 0), (gunX + i*xDiff/50, gunY + i*yDiff/50), 5)
        self.guntipX = gunX + xDiff
        self.guntipY = gunY + yDiff

    
    def move(self):
        if self.y >= self.screenheight - self.h:
            self.y = self.screenheight - self.h
            self.jumping = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 10:
            self.vel -= self.xaccel
            self.dir = "l"
        if keys[pygame.K_RIGHT] and self.x < self.screenwidth - self.w:
            self.vel += self.xaccel
            self.dir = "r"
        if keys[pygame.K_UP] and self.jumping == False:
            self.jumping = True
            self.yvel = 10
        if self.jumping == False:
            self.vel *= 0.95
        self.x += self.vel
        if self.x <= 0:
            self.x = 0
            self.vel = 0
        if self.x >= self.screenwidth - self.w:
            self.x = self.screenwidth - self.w
            self.vel = 0
        if self.jumping == True:
            self.yvel -= self.yaccel
            self.y -= self.yvel    
