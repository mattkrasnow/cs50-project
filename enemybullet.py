import pygame
import math

class EnemyBullet(object):
    # Constructor for Boss bullet objects that takes parameters of bullet position and bullet speed and direction
    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        bulletImg = pygame.image.load("mitbullet.png").convert_alpha() # load in the MIT bullet sprite and resize it
        self.img = pygame.transform.scale_by(bulletImg, 0.02)
        angle = math.atan(self.yvel/self.xvel)
        self.img = pygame.transform.rotate(self.img, 360-math.degrees(angle)) # rotate the image so it faces the correct direction towards the player
        self.w = self.img.get_width() # get the bullet's width and height for collisions
        self.h = self.img.get_height()

    # displays the Boss's bullet on screen as the MIT logo
    def display(self, screen):
        screen.blit(self.img, (self.x, self.y)) # draw the image onto the screen
    
    # move the bullet with respect to its velocity
    def move(self):
        self.x += self.xvel
        self.y += self.yvel
        
    # determine if the bullet is touching the enemy (the duck)
    def enemyCollision(self, enemy):
        if enemy.w + enemy.x > self.x and enemy.x < self.x + self.w and enemy.y + enemy.h > self.y and enemy.y < self.y + self.h: # use rectangle collision to see when enemy bullets collide with the player.
            return True
        return False