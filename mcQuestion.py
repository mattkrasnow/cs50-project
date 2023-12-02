import pygame
import random
from answer import Answer
from level import Level
from block import Block

class McQuestion():
    def __init__ (self, question, answers, correctIndex, screenWidth, screenHeight):
        blocks = [Block(0, 250, 200, 20), Block(600, 250, 200, 20), Block(300, 400, 200, 20), Block(200, 550, 100, 20), Block(500, 550, 100, 20)]
        self.level = Level([], blocks, 100000, 100000, screenWidth, screenHeight)
        positions = [[100, 100], [100, 500], [700, 100], [700, 500]]
        self.answers = []
        for i in range(4):
            ind = random.randint(0, 3-i)
            self.answers.append(Answer(answers[i], positions[ind][0], positions[ind][1], i == correctIndex))
            del positions[ind]
        self.q = question
        self.spawnX = 300
        self.spawnY = 200
        self.levelComplete = False
        self.levelFailed = False

    def display(self, screen):
        self.level.display(screen)

        for a in self.answers:
            a.display(screen)

        font = pygame.font.Font('SourceCodePro-SemiBold.ttf', 32)
        text = font.render(self.q, True, (200,200,200), (100,100,100))
        aRect = text.get_rect()
        aRect.center = (400, 100)
        screen.blit(text, aRect)
    
    def levelPhysics(self, duck):
        self.level.levelPhysics(duck)
        for a in self.answers:
            if a.duckCollision(duck):
                if a.correctness:
                    self.levelComplete = True
                else:
                    self.levelFailed = True

    # generate a level