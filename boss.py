import pygame
import random
import math
from hpbar import HPBar
from enemy import Enemy
from enemybullet import EnemyBullet

class Boss(object):
    # Constructor for Boss objects that takes parameters of the window dimensions (for proper physics)
    def __init__(self, screenwidth, screenheight):
        bossImg = pygame.image.load("bigbeaver.png").convert_alpha() # load the image for the boss sprite
        self.img = pygame.transform.scale_by(bossImg, 0.9) # resize the image and get the boss width and height based on its dimensions
        self.bossh = self.img.get_height()
        self.bossw = self.img.get_width()
        self.bossHP = 100
        self.bossMaxHP = 100
        self.hpBar = HPBar(100) # initialize an hp bar for the boss
        self.bossX = screenwidth/2
        self.bossY = 150
        angle = 6.283 * random.random() # choose a random angle and make the boss start moving at 5 pixels/frame in that direction
        self.bossXVel = 5 * math.cos(angle)
        self.bossYVel = 5 * math.sin(angle)
        self.levelComplete = False
        self.levelFailed = False
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.spawnX = 100
        self.spawnY = screenheight - 100
        self.bossEnemy = Enemy(self.bossX, self.bossY, screenwidth, screenheight) # create an enemy object that will handle collisions for the boss (and never display), and set its width and height so it is properly sized
        self.bossEnemy.w = self.bossw
        self.bossEnemy.h = self.bossh
        self.enemyHit = False
        self.hitDirection = 'r'
        self.enemyBullets = []
        self.bulletTime = 60

        self.populateEnemies()

    # Resets the health of boss if the user plays it multiple times 
    def populateEnemies(self):
        self.bossHP = 100
        self.bossMaxHP = 100
    
    # Bounces the boss around the screen and detects collisions with the duck
    def levelPhysics(self, duck):
        self.enemyHit = False # reset enemy hit
        self.bossX += self.bossXVel # move the boss in its direction of its velocity
        self.bossY += self.bossYVel
        if self.bossX <= 0: # if the boss hits left of screen, move it out and make it bounce to the right
            self.bossX = 0
            self.bossXVel = self.bossXVel * -1
        if self.bossY <= 0: # if the boss hits the top of the screen, it bounces down
            self.bossY = 0
            self.bossYVel = self.bossYVel * -1
        if self.bossX + self.bossw > self.screenwidth: # if the boss hits the right of the screen, it bounces left
            self.bossX = self.screenwidth - self.bossw
            self.bossXVel = self.bossXVel * -1
        if self.bossY + self.bossh > self.screenheight: # if the boss hits the left of the screen, it bounces right
            self.bossY = self.screenheight - self.bossh
            self.bossYVel = self.bossYVel * -1
        if self.bossCollision(duck): # check if the boss is colliding with the duck using the bossCollision method of this class
            self.enemyHit = True # if the duck does collide, record that so main can see the collision, and store what direction the boss hit the player in
            if self.bossX + self.bossw/2 > duck.x + duck.w/2:
                self.hitDirection = 'l'
            else:
                self.hitDirection = 'r'
        for bullet in self.enemyBullets: # loop over all the enemy bullets and move them
            bullet.move()
            if bullet.enemyCollision(duck): # if any of the enemy bullets hit the same player, record the collision and direction
                self.enemyHit = True
                if bullet.x + bullet.w/2 > duck.x + duck.w/2:
                    self.hitDirection = 'l'
                else:
                    self.hitDirection = 'r'
                self.enemyBullets.pop(self.enemyBullets.index(bullet)) # when bullets hit the player, remove them from the array so they dissapear
        self.bulletTime -= 1
        if self.bulletTime == 0: # use the same logic for a timer that makes the boss consistently shoot every two seconds
            self.bulletTime = 120
            bulletX = self.bossX + self.bossw/2 # define the bullet x and y
            bulletY = self.bossY + self.bossh/2
            xDiff = duck.x + duck.w/2 - bulletX
            yDiff = duck.y + duck.h/2 - bulletY
            normFactor = math.sqrt(xDiff*xDiff + yDiff*yDiff) # the bullets shoot towards the player, normalized to 8 pixels/frame
            xDiff = 8 * xDiff/normFactor
            yDiff = 8 * yDiff/normFactor
            self.enemyBullets.append(EnemyBullet(bulletX, bulletY, xDiff, yDiff)) # add the newly created bullet to the enemy bullets array

        return False # since the player never gets the "correct answer" on the first try, since this isn't a question, return False
    
    # returns true if the boss is touching the duck
    def bossCollision(self, duck):
        if duck.w + duck.x > self.bossX and duck.x < self.bossX + self.bossw and duck.y + duck.h > self.bossY and duck.y < self.bossY + self.bossh: # check if the player is collding with the boss 
            return True
        return False

    # Boss takes damage when the player's bullet is touching the boss
    def bulletCollisions(self, bullets, damage):
        self.bossEnemy.x = self.bossX # move the boss enemy to properly handle collisions
        self.bossEnemy.y = self.bossY
        for bullet in bullets: # for every player bullet, check if it is colliding with the boss
            if bullet.enemyCollision(self.bossEnemy):
                self.bossHP -= damage # if the bullet is hitting the boss, decrease the boss's health, and remove that bullet from the bullets array
                bullets.pop(bullets.index(bullet))
                if self.bossHP <= 0:
                    self.levelComplete = True # if the boss no longer has any health, the level is complete
        
    # displays the boss on the screen as the MIT logo with a HP bar
    def display(self, screen):
        for bullet in self.enemyBullets: # draw each bullet using the enemyBullet display method
            bullet.display(screen)
        screen.blit(self.img, (self.bossX, self.bossY)) # draw the boss image onto the screen
        self.hpBar.hp = self.bossHP
        self.hpBar.display(screen, self.bossX + self.bossw/2, self.bossY - 30) # use the hpbar display method to draw it over the boss