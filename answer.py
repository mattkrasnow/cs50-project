import pygame 
import random

class Answer():
    # constructor that sets the answer objects
    def __init__(self, input, x, y, isCorrect):
        self.answerText = input
        self.x = x - 25
        self.y = y - 25
        self.w = 50
        self.h = 50
        self.correctness = isCorrect

    def duckCollision(self, duck):
        # return  true if the duck is touching the answer object; otherwise return false
        # check if the duck is touching the answer object
        if duck.w + duck.x > self.x and duck.x < self.x + self.w and duck.y + duck.h > self.y and duck.y < self.y + self.h:
            return True
        return False
    
    # display answer objects
    def display(self, screen):
        font = pygame.font.Font('SourceCodePro-SemiBold.ttf', 32)
        text = font.render(self.answerText, True,  (0,255,0), (100,100,100))
        aRect = text.get_rect()
        aRect.center = (self.x + 25, self.y - 25)
        screen.blit(text, aRect)
        pygame.draw.rect(screen, (255*random.random(),255*random.random(),255*random.random()), (self.x, self.y, self.w, self.h))