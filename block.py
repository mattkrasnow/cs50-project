import pygame

class Block(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def display(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.w, self.h))

    def objectCollision(self, object):
        if object.x + object.w <= self.x or object.x >= self.x + self.w:
            if object.jumping == False:
                #object.jumping = True
                object.yvel = 0
        if object.y <= self.y-object.h-5 or object.y >= self.y+self.h: 
            if object.jumping == False:
                #object.jumping = True
                object.yvel = 0
        if object.x >= self.x - object.w and object.x <= self.x + self.w and object.y >= self.y - object.h + 5 and object.y < self.y + self.h:
            object.yvel = 0
            
            #object.y = self.y + self.h
        if object.x >= self.x - object.w and object.x <= self.x + self.w and object.y + object.yvel >= self.y - object.h + 5 and object.y + object.yvel < self.y + self.h:
            object.yvel = 0
            #object.y = self.y + self.h
        if object.x >= self.x - object.w and object.x <= self.x + self.w and object.y < self.y - 0.9*object.h and object.y > self.y-object.h:
            object.y = self.y - object.h-1
            object.jumping = False
            object.yvel = 0
        if object.x >= self.x - object.w and object.x <= self.x + self.w and object.y + object.h < self.y and object.y + object.h > self.y - 5:
            object.jumping = False
        
        if object.x - 10 >= self.x - object.w and object.x + 10 <= self.x + self.w and object.y < self.y + self.h and object.y + object.h >= self.y + self.h - 12:
            object.yvel = 0
            object.y = self.y + self.h
        elif object.x >= self.x - object.w-1 and object.x + 40 <= self.x + self.w and object.y < self.y + self.h and object.y + object.h >= self.y:
            object.x = self.x - object.w - 1
            object.vel = 0
        if object.x <= self.x + self.w and object.x > self.x + object.w and object.y < self.y + self.h and object.y + object.h >= self.y:
            object.x = self.x + self.w + 1
            object.vel = 0