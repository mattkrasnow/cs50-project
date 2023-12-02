import pygame
import random
from answer import Answer
from level import Level
from block import Block

class McQuestion():
    def __init__ (self, question, answers, correctIndex, screenWidth, screenHeight):
        blocks = [Block(0, 250, 200, 20), Block(600, 250, 200, 20), Block(300, 400, 200, 20), Block(200, 550, 100, 20), Block(500, 550, 100, 20)]
        self.level = Level([], blocks, 100000, 100000, screenWidth, screenHeight)
        self.a1 = Answer(answers[0], 100, 100, correctIndex == 1 )
        self.a2 = Answer(answers[1], 100, 500, correctIndex == 2 )
        self.a3 = Answer(answers[2], 700, 100, correctIndex == 3 )
        self.a4 = Answer(answers[3], 700, 500, correctIndex == 4 )
        self.q = question
        self.spawnX = 300
        self.spawnY = 200
        self.levelComplete = False

    def display(self, screen):
        self.level.display(screen)

        self.a1.display(screen)
        self.a2.display(screen)
        self.a3.display(screen)
        self.a4.display(screen)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.q, True,  (0,255,0), (0,0,128))
        aRect = text.get_rect()
        screen.blit(text, aRect)
    def levelPhysics(self, duck):
        self.level.levelPhysics(duck)

    # generate a level