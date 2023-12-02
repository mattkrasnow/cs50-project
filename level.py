import pygame
from block import Block
from enemy import Enemy
from answer import Answer


class Level(object):
    def __init__(self, enemyPos, blocks, exitX, exitY, screenwidth, screenheight):
        self.enemyPos = enemyPos
        self.enemies = []
        self.blocks = blocks
        self.exit = Answer("", exitX, exitY, True)
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.levelComplete = False
        self.levelFailed = False
        self.spawnX = 100
        self.spawnY = 400
        self.enemyHit = False
        self.populateEnemies()
    
    def populateEnemies(self):
        self.enemies = []
        for pos in self.enemyPos:
            self.enemies.append(Enemy(pos[0], pos[1], self.screenwidth, self.screenheight))
    
    def levelPhysics(self, duck):
        for block in self.blocks:
            block.objectCollision(duck)
        self.enemyHit = False
        for enemy in self.enemies:
            if enemy.y >= self.screenheight - enemy.h:
                enemy.y = self.screenheight - enemy.h
                enemy.jumping = False
            enemy.move(duck)
            enemy.jumping = True   
            for block in self.blocks:
                block.objectCollision(enemy)
            if enemy.duckCollision(duck):
                self.enemyHit = True
        
        if(self.exit.duckCollision(duck)):
            self.levelComplete = True
        
    def bulletCollisions(self, bullets):
        for enemy in self.enemies:
            for bullet in bullets:
                if bullet.enemyCollision(enemy):
                    enemy.hp -= 1
                    bullets.pop(bullets.index(bullet))
                    if enemy.hp == 0:
                        self.enemies.pop(self.enemies.index(enemy))
        
    def display(self, screen):
        for block in self.blocks:
            block.display(screen)
        for enemy in self.enemies:
            enemy.display(screen)
        if not self.levelComplete:
            self.exit.display(screen)