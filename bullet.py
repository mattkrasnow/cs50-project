import pygame

class Bullet(object):
    # Constructor that takes in x and y positions and the direction/speed of the bullet
    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        bulletImg = pygame.image.load("newbullet.png").convert_alpha()
        self.img = pygame.transform.scale_by(bulletImg, 0.2)
        self.w = self.img.get_width()
        self.h = self.img.get_height()

    # displays the bullet on scrreen as an image
    def display(self, screen):
        screen.blit(self.img, (self.x, self.y))
    
    # moves the bullet in the direction and speed of the set velocity
    def move(self):
        self.x += self.xvel
        self.y += self.yvel
        
    # determines if the bullet is touching an enemy    
    def enemyCollision(self, enemy):
        if enemy.w + enemy.x > self.x and enemy.x < self.x + self.w and enemy.y + enemy.h > self.y and enemy.y < self.y + self.h:
            return True
        return False