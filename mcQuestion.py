import pygame
import random
from answer import Answer

font = pygame.font.Font('freesansbold.ttf', 32)
class Mqquestion():
    def __init__ (self, question, answers, correctIndex):
        self.a1 = Answer(answers[0], 100, 100, correctIndex == 1 )
        self.a2 = Answer(answers[1], 100, 500, correctIndex == 2 )
        self.a3 = Answer(answers[2], 500, 100, correctIndex == 3 )
        self.a4 = Answer(answers[3], 500, 500, correctIndex == 4 )
        self.q = question

def display(self, screen):
    
    text = font.render(self.a1.answerText, True,  (0,255,0), (0,0,128))
    aRect = text.get_rect()
    screen.blit(text, aRect)
    self.a1.display()
    

    text = font.render(self.a2.answerText, True,  (0,255,0), (0,0,128))
    aRect = text.get_rect()
    screen.blit(text, aRect)        
    self.a2.display()


    text = font.render(self.a3.answerText, True,  (0,255,0), (0,0,128))
    aRect = text.get_rect()
    screen.blit(text, aRect)  
    self.a3.display()


    text = font.render(self.a3.answerText, True,  (0,255,0), (0,0,128))
    aRect = text.get_rect()
    screen.blit(text, aRect)  
    self.a4.display()


    text = font.render(self.q, True,  (0,255,0), (0,0,128))
    aRect = text.get_rect()
    screen.blit(text, aRect)

# generate a level