import pygame
from hpbar import HPBar
import math

class Duck(object):
    # constructor for the player that takes the screen dimensions (for physics)
    def __init__(self, x, y, screenwidth, screenheight):
        self.x = x
        self.y = y
        self.vel = 0
        self.xaccel = 0.2
        self.jumping = False
        self.yaccel = 0.3
        self.yvel = 0
        self.dir = 'r'
        self.hp = 10
        self.maxHp = 10 # initialize an hpbar for the duck with 10 health
        self.hpBar = HPBar(10)
        self.guntipX = self.x # initialize a gun tip location that will be updated later
        self.guntipY = self.y

        duckImg = pygame.image.load("cs50duck.png").convert_alpha() # load in the duck image, and resize to the proper size
        self.imgR = pygame.transform.scale_by(duckImg, 0.2)
        self.imgL = self.imgR.copy() 
        self.imgL = pygame.transform.flip(self.imgL, flip_x=True, flip_y=False) # for when the duck faces the other direction, we have a reversed image
        self.h = self.imgR.get_height() # get the width and height of the duck for proper collisions
        self.w = self.imgR.get_width()
        self.screenwidth = screenwidth
        self.screenheight = screenheight

    # displays the duck on screen as an image with "a", facing the direction of movement
    def display(self, win):
        gunX = self.x + self.w/2 # location for the base of the gun
        gunY = self.y + 3*self.h/4
        if self.dir == 'r':
            win.blit(self.imgR, (self.x, self.y)) # draw the player facing right
            gunX += 20 # move the gun to the right if player is facing right
        else:
            win.blit(self.imgL, (self.x, self.y)) # draw the player facing left
            gunX -= 20 # move the gun to the left if the player is facing left
        self.hpBar.hp = self.hp 
        self.hpBar.display(win, self.x + self.w/2, self.y - 30) # update the hp bar hp and display it
        
        mouseX, mouseY = pygame.mouse.get_pos() # get mouse position for gun drawing
        xDiff = mouseX - gunX
        yDiff = mouseY - gunY
        normFactor = math.sqrt(xDiff * xDiff + yDiff * yDiff) 
        xDiff = 20 * xDiff / normFactor # normalize the length of the gun so it is always 20 pixels towards the pixel
        yDiff = 20 * yDiff / normFactor
        for i in range(0, 50):
            pygame.draw.circle(win, (0, 0, 0), (gunX + i*xDiff/50, gunY + i*yDiff/50), 5) # draw a number of circles between the gun base and tip so it appears as a cylinder
        self.guntipX = gunX + xDiff # move gun tip position so that new bullets appear to come out of the gun
        self.guntipY = gunY + yDiff

    
    # move the duck with respect to the key that has been pressed
    def move(self):
        if self.y >= self.screenheight - self.h: # if the player is on the bottom of the screen, they are not in the air or jumping
            self.y = self.screenheight - self.h
            self.jumping = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 10: # if the player is clicking A, they accelerate to the left (And the sprite turns left)
            self.vel -= self.xaccel
            self.dir = "l"
        if keys[pygame.K_d] and self.x < self.screenwidth - self.w: # if the player is clicking D, they accelerate to the right (and the sprite turns right)
            self.vel += self.xaccel
            self.dir = "r"
        if keys[pygame.K_w] and self.jumping == False: # if the player is pressing W, and they are currently not jumping, meaning they are on the ground, they jump
            self.jumping = True
            self.yvel = 10
        if self.jumping == False: # The player slows down when on the ground (friction)
            self.vel *= 0.95
        self.x += self.vel # the player moves based on their x velocity
        if self.x <= 0: # collision with the left side of the screen
            self.x = 0
            self.vel = 0
        if self.x >= self.screenwidth - self.w: # collision with the right side of the screen
            self.x = self.screenwidth - self.w
            self.vel = 0
        if self.jumping == True: # if the player is jumping, they accelerate downwards and move based on their vertical velocity
            self.yvel -= self.yaccel
            self.y -= self.yvel    
