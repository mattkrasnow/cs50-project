import pygame
from block import Block
from enemy import Enemy
from answer import Answer


class Level(object):
    def __init__(self, enemyPos, blocks, exitX, exitY, screenwidth, screenheight, spawnX, spawnY, disptext=""):
        self.enemyPos = enemyPos
        self.enemies = []
        self.blocks = blocks
        self.exit = Answer("", exitX, exitY, True)
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.levelComplete = False
        self.levelFailed = False
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.enemyHit = False
        self.hitDirection = 'r'
        self.text = disptext
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
                self.hitDirection = enemy.dir
        
        if(self.exit.duckCollision(duck)):
            self.levelComplete = True
        return False
        
    def bulletCollisions(self, bullets, damage):
        for enemy in self.enemies:
            for bullet in bullets:
                if bullet.enemyCollision(enemy):
                    enemy.hp -= damage
                    if bullet.xvel <= 0:
                        enemy.vel = -2
                    else:
                        enemy.vel = 2
                    enemy.yvel += 4
                    enemy.jumping = True
                    enemy.y -= 8
                    bullets.pop(bullets.index(bullet))
                    if enemy.hp <= 0:
                        self.enemies.pop(self.enemies.index(enemy))
        
    def display(self, screen):
        font = pygame.font.Font('SourceCodePro-SemiBold.ttf', 12)
        text = font.render(self.text, True,  (0,255,0), (50,50,50))
        aRect = text.get_rect()
        aRect.center = (self.screenwidth/2, 100)
        screen.blit(text, aRect)
        for block in self.blocks:
            block.display(screen)
        for enemy in self.enemies:
            enemy.display(screen)
        if not self.levelComplete:
            self.exit.display(screen)