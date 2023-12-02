import pygame 
import random

class Answer():
    # constructor that sets the answer objects
    def __innit__(self, input, x, y, isCorrect):
        self.answerText = input
        self.x = x - 25
        self.y = y - 25
        self.w = 50
        self.h = 50
        self.correctnesss = isCorrect

    def duckCollision(self, duck):
        # return  true if the duck is touching the answer object; otherwise return false
        # check if the duck is touching the answer object
        if duck.w + duck.x > self.x and duck.x < self.x + self.w and duck.y + duck.h < self.h and duck.y > self.y + self.h:
            return True
        return False
    
    # display answer objects
    def display(self, screen):
        pygame.draw.rect(screen, (256*random.random(),256*random.random(),256*random.random()), self.x, self.y, self.w, self.h)