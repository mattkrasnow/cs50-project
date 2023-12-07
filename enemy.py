import pygame
from hpbar import HPBar

class Enemy(object):
    # Constructor for enemy objects that takes in the enemy position and screen dimensions (for physics) 
    def __init__(self, x, y, screenwidth, screenheight):
        self.x = x
        self.y = y
        self.vel = 0
        self.xaccel = 0.06
        self.jumping = False
        self.yaccel = 0.3
        self.yvel = 0
        self.hp = 6
        self.maxHp = 6 # initialize an hp bar for the enemy
        self.hpBar = HPBar(6)

        beaverImg = pygame.image.load("beaversprite.png").convert_alpha() # load in enemy image and size it correctly
        self.imgL = pygame.transform.scale_by(beaverImg, 0.3)
        self.imgR = self.imgL.copy()
        self.imgR = pygame.transform.flip(self.imgR, flip_x=True, flip_y=False) # flip enemy image to face the player
        self.h = self.imgR.get_height() # get enemy width and height for collisions
        self.w = self.imgR.get_width()
        self.dir = 'r'
        self.screenwidth = screenwidth
        self.screenheight = screenheight

    # displays the MIT badger on screen, facing the duck
    def display(self, win):
        if self.dir == 'r': # draw enemy beaver facing left or right, depending on what direction it is facing
            win.blit(self.imgR, (self.x, self.y))
        else:
            win.blit(self.imgL, (self.x, self.y))
        self.hpBar.hp = self.hp
        self.hpBar.display(win, self.x + self.w/2, self.y - 30) # update hp and draw the hpbar
    
    # move the enemy in the direction of the duck
    def move(self, duck):
        if self.y >= self.screenheight - self.h: # make beavers stop falling at bottom of screen, and allow them to jump there. 
            self.y = self.screenheight - self.h
            self.jumping = False
        if duck.x + duck.w/2 > self.x + self.w/2: # check if the duck is to the left or right of the enemy, and face towards it (as if a platyer is pressing A or D)
            self.dir = 'r'
            if self.x < self.screenwidth - self.w:
                self.vel += self.xaccel
        else:
            self.dir = 'l'
            if self.x > 10:
                self.vel -= self.xaccel
        if duck.y + duck.h < self.y + self.h and self.jumping == False: # if the duck is above the enemy, and it is able to jump, it jumps
            self.jumping = True
            self.yvel = 10
        if self.jumping == True: # as long as the enemy is jumping, it accelerates downwards and moves based on its vertical velocity
            self.yvel -= self.yaccel
            self.y -= self.yvel  

        if self.jumping == False: # enemies also have friction on the ground
            self.vel *= 0.95
        self.x += self.vel # move based on x velocity in the x direction
        if self.x <= 0: # collision with the left side of the screen
            self.x = 0
            self.vel = 0
        if self.x >= self.screenwidth - self.w: # collision with the right side of the screen
            self.x = self.screenwidth - self.w
            self.vel = 0
    # determine if the enemy is touching the duck    
    def duckCollision(self, duck):
        if duck.w + duck.x > self.x and duck.x < self.x + self.w and duck.y + duck.h > self.y and duck.y < self.y + self.h: # use rectangle collision to detect when the player and the enemy are colliding. 
            return True
        return False