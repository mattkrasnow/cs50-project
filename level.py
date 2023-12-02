import pygame
from block import Block
from enemy import Enemy
from answer import Answer


class Level(object):
    def __init__(self, enemies, blocks, exitX, exitY, screenwidth, screenheight):
        self.enemies = enemies
        self.blocks = blocks
        self.exit = Answer("", exitX, exitY, True)
        self.screenwidth = screenwidth
        self.screenheight = screenheight
    
    def levelPhysics(self, duck):
        for block in self.blocks:
            block.objectCollision(duck)
        for enemy in self.enemies:
            if enemy.y >= self.screenheight - enemy.h:
                enemy.y = self.screenheight - enemy.h
                enemy.jumping = False
            enemy.move(duck)
            enemy.jumping = True   
            for block in self.blocks:
                block.objectCollision(enemy)
        
    def display(self, screen):
        for block in self.blocks:
            block.display(screen)
        for enemy in self.enemies:
            enemy.display(screen)