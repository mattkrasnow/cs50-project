import pygame
import random
import math
from hpbar import HPBar
from enemy import Enemy

class Boss(object):
    def __init__(self, screenwidth, screenheight):
        bossImg = pygame.image.load("bigbeaver.png").convert_alpha()
        self.img = pygame.transform.scale_by(bossImg, 0.9)
        self.bossh = self.img.get_height()
        self.bossw = self.img.get_width()
        self.bossHP = 100
        self.bossMaxHP = 100
        self.hpBar = HPBar(100)
        self.bossX = screenwidth/2
        self.bossY = 150
        angle = 6.283 * random.random()
        self.bossXVel = 5 * math.cos(angle)
        self.bossYVel = 5 * math.sin(angle)
        self.levelComplete = False
        self.levelFailed = False
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.spawnX = 100
        self.spawnY = screenheight - 100
        self.blocks = []
        self.bossEnemy = Enemy(self.bossX, self.bossY, screenwidth, screenheight)
        self.bossEnemy.w = self.bossw
        self.bossEnemy.h = self.bossh


        self.populateEnemies()

    def populateEnemies(self):
        self.bossHP = 100
        self.bossMaxHP = 100
    
    def levelPhysics(self, duck):
        for block in self.blocks:
            block.objectCollision(duck)
        self.enemyHit = False
        self.bossX += self.bossXVel
        self.bossY += self.bossYVel
        if self.bossX <= 0:
            self.bossX = 0
            self.bossXVel = self.bossXVel * -1
        if self.bossY <= 0:
            self.bossY = 0
            self.bossYVel = self.bossYVel * -1
        if self.bossX + self.bossw > self.screenwidth:
            self.bossX = self.screenwidth - self.bossw
            self.bossXVel = self.bossXVel * -1
        if self.bossY + self.bossh > self.screenheight:
            self.bossY = self.screenheight - self.bossh
            self.bossYVel = self.bossYVel * -1
        return False


    def bulletCollisions(self, bullets, damage):
        self.bossEnemy.x = self.bossX
        self.bossEnemy.y = self.bossY
        for bullet in bullets:
            if bullet.enemyCollision(self.bossEnemy):
                self.bossHP -= damage
                bullets.pop(bullets.index(bullet))
                if self.bossHP == 0:
                    self.levelComplete = True
        pass

    def display(self, screen):
        for block in self.blocks:
            block.display(screen)
        screen.blit(self.img, (self.bossX, self.bossY))
        self.hpBar.hp = self.bossHP
        self.hpBar.display(screen, self.bossX + self.bossw/2, self.bossY - 30)