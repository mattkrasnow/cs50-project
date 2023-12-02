import pygame

class Block(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def display(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.w, self.h))

    def duckCollision(self, duck):
        if duck.x <= self.x-20 or duck.x >= self.x + self.w:
            if duck.jumping == False:
                #duck.jumping = True
                duck.yvel = 0
        if duck.y <= self.y-duck.h-5 or duck.y >= self.y+self.h: 
            if duck.jumping == False:
                #duck.jumping = True
                duck.yvel = 0
        if duck.x >= self.x - duck.w and duck.x <= self.x + self.w and duck.y >= self.y - duck.h + 5 and duck.y < self.y + self.h:
            duck.yvel = 0
            
            #duck.y = self.y + self.h
        if duck.x >= self.x - duck.w and duck.x <= self.x + self.w and duck.y + duck.yvel >= self.y - duck.h + 5 and duck.y + duck.yvel < self.y + self.h:
            duck.yvel = 0
            #duck.y = self.y + self.h
        if duck.x >= self.x - duck.w and duck.x <= self.x + self.w and duck.y < self.y - 0.9*duck.h and duck.y > self.y-duck.h:
            duck.y = self.y - duck.h-1
            duck.jumping = False
            duck.yvel = 0
        if duck.x >= self.x - duck.w and duck.x <= self.x + self.w and duck.y + duck.h < self.y and duck.y + duck.h > self.y - 5:
            duck.jumping = False
        if duck.x >= self.x - duck.w-1 and duck.x + 40 <= self.x + self.w and duck.y < self.y + self.h and duck.y + duck.h >= self.y:
            duck.x = self.x - duck.w - 1
            duck.vel = 0
        if duck.x <= self.x + self.w and duck.x > self.x + duck.w and duck.y < self.y + self.h and duck.y + duck.h >= self.y:
            duck.x = self.x + self.w + 1
            duck.vel = 0