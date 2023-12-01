import pygame

class Duck(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.xaccel = 0.2
        self.jumping = False
        self.yaccel = 0.3
        self.yvel = 0
        self.dir = 'r'
        duckImg = pygame.image.load("cs50duck.png").convert_alpha()
        self.img = pygame.transform.scale_by(duckImg, 0.3)
        self.h = self.img.get_height()
        self.w = self.img.get_width()

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 10:
            self.vel -= self.xaccel
            self.dire = "l"
        if keys[pygame.K_RIGHT] and self.x < 1920 - self.w:
            self.vel += self.xaccel
            self.dire = "r"
        if keys[pygame.K_UP] and self.jumping == False:
            self.jumping = True
            self.yvel = 12
        if self.jumping == False:
            self.vel *= 0.95
        self.x += self.vel
        if self.x <= 0:
            self.x = 0
            self.vel = 0
        if self.x >= 1920 - self.w:
            self.x = 1920 - self.w
            self.vel = 0
        if self.jumping == True:
            self.yvel -= self.yaccel
            self.y -= self.yvel    
