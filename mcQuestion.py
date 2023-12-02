import pygame
import random
from answer import Answer
from level import Level
from block import Block

class McQuestion():
    def __init__ (self, question, answers, correctIndex, screenWidth, screenHeight):
        blocks = [Block(0, screenHeight-350, 200, 20), Block(screenWidth - 200, screenHeight-350, 200, 20), Block(screenWidth/2 - 100, screenHeight-200, 200, 20), Block(screenWidth/2-200, screenHeight-50, 100, 20), Block(screenWidth/2+100, screenHeight-50, 100, 20)]
        self.level = Level([], blocks, 100000, 100000, screenWidth, screenHeight)
        positions = [[100, 100], [100, screenHeight-100], [screenWidth-100, 100], [screenWidth-100, screenHeight-100]]
        self.answers = []
        for i in range(4):
            ind = random.randint(0, 3-i)
            self.answers.append(Answer(answers[i], positions[ind][0], positions[ind][1], i == correctIndex))
            del positions[ind]
        self.q = question
        self.spawnX = screenWidth/2
        self.spawnY = 200
        self.levelComplete = False
        self.levelFailed = False
        self.enemyHit = False
        self.screenwidth = screenWidth
        self.screenheight = screenHeight


    def display(self, screen):
        self.level.display(screen)

        for a in self.answers:
            a.display(screen)

        font = pygame.font.Font('SourceCodePro-SemiBold.ttf', 12)
        text = font.render(self.q, True, (200,200,200), (100,100,100))
        aRect = text.get_rect()
        aRect.center = (self.screenwidth/2, 100)
        screen.blit(text, aRect)
    
    def levelPhysics(self, duck):
        self.level.levelPhysics(duck)
        for a in self.answers:
            if a.duckCollision(duck):
                if a.correctness:
                    self.levelComplete = True
                else:
                    self.levelFailed = True
    
    def bulletCollisions(self, bullets):
        pass

    def populateEnemies(self):
        pass

    # generate a level