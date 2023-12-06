import pygame

class Boss(object):
    def __init__(self):
        bossImg = pygame.image.load("bigbeaver.png").convert_alpha()
        self.img = pygame.transform.scale_by(bossImg, 0.3)
        self.h = self.img.get_height()
        self.w = self.img.get_width()