import pygame

class HPBar(object):
    def __init__(self, hpamt):
        self.maxHp = hpamt
        self.hp = hpamt
        self.w = 10 * self.maxHp
        self.h = 10
    
    def display(self, screen, centerX, centerY):
        if self.hp > 0:
            pygame.draw.rect(screen, (0, 0, 0), (centerX - self.w/2, centerY - self.h/2, self.w, self.h))
            pygame.draw.rect(screen, (255 - 255*(self.hp/self.maxHp), 255*(self.hp/self.maxHp), 0), (centerX - self.w/2 + 2, centerY - self.h/2 + 2, self.hp * (self.w - 4) / self.maxHp, self.h - 4))