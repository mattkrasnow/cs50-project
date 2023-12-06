import pygame
import random
import math
from hpbar import HPBar
from enemy import Enemy
from enemybullet import EnemyBullet

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
        self.enemyHit = False
        self.hitDirection = 'r'
        self.enemyBullets = []
        self.bulletTime = 60

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
        if self.bossCollision(duck):
            self.enemyHit = True
            if self.bossX + self.bossw/2 > duck.x + duck.w/2:
                self.hitDirection = 'l'
            else:
                self.hitDirection = 'r'
        for bullet in self.enemyBullets:
            bullet.move()
            if bullet.enemyCollision(duck):
                self.enemyHit = True
                if bullet.x + bullet.w/2 > duck.x + duck.w/2:
                    self.hitDirection = 'l'
                else:
                    self.hitDirection = 'r'
                self.enemyBullets.pop(self.enemyBullets.index(bullet))
        self.bulletTime -= 1
        if self.bulletTime == 0:
            self.bulletTime = 120
            bulletX = self.bossX + self.bossw/2
            bulletY = self.bossY + self.bossh/2
            xDiff = duck.x + duck.w/2 - bulletX
            yDiff = duck.y + duck.h/2 - bulletY
            normFactor = math.sqrt(xDiff*xDiff + yDiff*yDiff)
            xDiff = 8 * xDiff/normFactor
            yDiff = 8 * yDiff/normFactor
            self.enemyBullets.append(EnemyBullet(bulletX, bulletY, xDiff, yDiff))


        return False
    
    def bossCollision(self, duck):
        if duck.w + duck.x > self.bossX and duck.x < self.bossX + self.bossw and duck.y + duck.h > self.bossY and duck.y < self.bossY + self.bossh:
            return True
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
        

    def display(self, screen):
        for block in self.blocks:
            block.display(screen)
        for bullet in self.enemyBullets:
            bullet.display(screen)
        screen.blit(self.img, (self.bossX, self.bossY))
        self.hpBar.hp = self.bossHP
        self.hpBar.display(screen, self.bossX + self.bossw/2, self.bossY - 30)