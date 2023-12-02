import pygame

class Bullet(object):
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.v = 10
        bulletImg = pygame.image.load("laserbullet.png").convert_alpha()
        self.imgR = pygame.transform.scale_by(bulletImg, 0.2)
        self.imgL = self.imgR.copy()
        self.imgL = pygame.transform.flip(self.imgL, flip_x=True, flip_y=False)
        self.w = self.imgR.get_width()
        self.h = self.imgR.get_height()

    def display(self, screen):
        if self.d == 'l':
            screen.blit(self.imgL, (self.x, self.y))
        else:
            screen.blit(self.imgR, (self.x, self.y))
    
    def move(self):
        if self.d == "l":
            self.x -= self.v
        else:
            self.x += self.v
        
    def enemyCollision(self, enemy):
        if enemy.w + enemy.x > self.x and enemy.x < self.x + self.w and enemy.y + enemy.h > self.y and enemy.y < self.y + self.h:
            return True
        return False