import pygame

class Block(object):
    # Constructor for block objects that takes x and y positions and w and h dimensions (width,height)
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # displays the block object on the screen by drawing a black rectangle
    def display(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.w, self.h)) 

    # detects when the block is colliding with the duck or an enemy
    def objectCollision(self, object):
        if object.jumping == False: # if the player is touching the ground, automatically set their y velocity to zero.
            object.yvel = 0

        if object.x - 10 >= self.x - object.w and object.x + 10 <= self.x + self.w and object.y < self.y + self.h and object.y + object.h >= self.y + self.h - 12: # make sure the player collides witht he bottom of the block and not get moved on top of it when approaching from the bottom
            object.yvel = 0
            object.y = self.y + self.h

        if object.x  + object.w >= self.x and object.x <= self.x + self.w and object.y + object.h + object.yvel >= self.y and object.y + object.h < self.y + object.yvel + 1: # check if the player is inside a block, or falling inside a block, and if so, reset their y velocity and place them on top of the block
            object.yvel = 0
            object.y = self.y - object.h

        if object.x + object.w >= self.x and object.x <= self.x + self.w and object.y + 0.9 * object.h < self.y and object.y + object.h > self.y: # check if the player has fallen into the block a little. If so, place them above the block.
            object.y = self.y - object.h-1
            object.jumping = False
            object.yvel = 0
                
        if object.x + object.w >= self.x and object.x <= self.x + self.w and object.y + object.h < self.y and object.y + object.h > self.y - 5: # check if the player is standing on top of the block. If so, turn off jumping to the code knows they are grounded 
            object.jumping = False
        
        if object.x + object.w + 1 >= self.x and object.x + object.w/2 <= self.x + self.w/2 and object.y < self.y + self.h and object.y + object.h >= self.y: # check if the player is colliding with or slightly in the left side of the block. If so, move them out of the block and reset their x velocity
            object.x = self.x - object.w - 1
            object.vel = 0
        elif object.x - 1 <= self.x + self.w and object.x + object.w/2 >= self.x + self.w/2 and object.y < self.y + self.h and object.y + object.h > self.y: # check if the player is colliding with or slightly in the right side of the block. If so, move them out of the block and reset their x velocity
            object.x = self.x + self.w + 1
            object.vel = 0