import pygame
import random
from answer import Answer


class Mqquestion():
    def __init__ (self, question, answers, correctIndex):
        self.a1 = Answer(answers[0], 100, 100, correctIndex == 1 )
        self.a2 = Answer(answers[1], 100, 500, correctIndex == 2 )
        self.a3 = Answer(answers[2], 500, 100, correctIndex == 3 )
        self.a4 = Answer(answers[3], 500, 500, correctIndex == 4 )
        self.q = question

def display(self, screen):

    self.a1.display()
    self.a2.display()
    self.a3.display()
    self.a4.display()

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(self.q, True,  (0,255,0), (0,0,128))
    aRect = text.get_rect()
    screen.blit(text, aRect)

# generate a level