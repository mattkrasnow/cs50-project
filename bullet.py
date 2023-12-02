import pygame

class Bullet(object):
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.r = 4
        self.v = 10

    def display(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.r)
    
    def move(self):
        if self.d == "l":
            self.x -= self.v
        else:
            self.x += self.v