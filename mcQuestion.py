import pygame
import random
from answer import Answer
from level import Level
from block import Block

class McQuestion():
    # Constructor for question "levels". Parameters: question asked to player, possible answers, the index of the correct answer, and the window dimensions
    def __init__ (self, question, answers, correctIndex, screenWidth, screenHeight):
        self.spawnX = screenWidth/2
        self.spawnY = 200
        blocks = [Block(0, screenHeight-350, 200, 20), Block(screenWidth - 200, screenHeight-350, 200, 20), Block(screenWidth/2 - 100, screenHeight-200, 200, 20), Block(screenWidth/2-200, screenHeight-50, 100, 20), Block(screenWidth/2+100, screenHeight-50, 100, 20)]
        self.level = Level([], blocks, 100000, 100000, screenWidth, screenHeight, self.spawnX, self.spawnY, disptext=question)
        positions = [[100, 150], [100, screenHeight-100], [screenWidth-100, 150], [screenWidth-100, screenHeight-100]]
        self.answers = []
        for i in range(4):
            ind = random.randint(0, 3-i)
            self.answers.append(Answer(answers[i], positions[ind][0], positions[ind][1], i == correctIndex))
            del positions[ind]
        self.levelComplete = False
        self.levelFailed = False
        self.enemyHit = False
        self.screenwidth = screenWidth
        self.screenheight = screenHeight
        self.questionAnswered = False

    # display the questions and answers on the screen
    def display(self, screen):
        self.level.display(screen)

        for a in self.answers:
            a.display(screen)
    
    # define if the duck has answered the question correctly and duck's movement
    def levelPhysics(self, duck):
        self.level.levelPhysics(duck)
        for a in self.answers:
            if a.duckCollision(duck):
                if a.correctness:
                    self.levelComplete = True
                    if self.questionAnswered == False:
                        self.questionAnswered = True
                        return True
                else:
                    self.levelFailed = True
                    self.questionAnswered = True
        return False
    
    # Prevents developer errors if the developer treats mcquestion objects as levels
    def bulletCollisions(self, bullets, damage):
        pass
    
    # Prevents developer errors if the developer treats mcquestion objects as levels
    def populateEnemies(self):
        pass

    # generate a level