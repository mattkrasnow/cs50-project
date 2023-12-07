import pygame 
import random
import math

class Answer():
    # constructor that sets the answer objects
    def __init__(self, input, x, y, isCorrect):
        self.answerText = input # sets the text above the portal if this exit is for a multiple choice question
        self.w = 60
        self.h = 150
        self.x = x - self.w/2
        self.y = y - self.h/2
        self.r = max(self.w, self.h)
        self.correctness = isCorrect # if this is a multiple choice question, store whether this is the correct or incorrect answer (exits on normal levels always have a value of True)
        self.cycle = 0

    def duckCollision(self, duck):
        # return  true if the duck is touching the answer object; otherwise return false
        # check if the duck is touching the answer object
        if duck.w + duck.x > self.x and duck.x < self.x + self.w and duck.y + duck.h > self.y and duck.y < self.y + self.h:
            return True
        return False
    
    # display answer objects
    def display(self, screen):
        font = pygame.font.Font('SourceCodePro-SemiBold.ttf', 10)
        text = font.render(self.answerText, True,  (0,255,0), (50,50,50))
        aRect = text.get_rect()
        aRect.center = (self.x + self.w/2, self.y - 25) # center the text above the portal
        screen.blit(text, aRect) # draw the text onto the screen
        self.cycle += 1 # increment cycle for the portal effect
        temp = pygame.Surface((self.w, self.h))
        for i in range(self.r): # to get the portal effect, a number of circles are drawn onto a separate pygame "surface" which is the exact dimensions of the portal, which is then put onto the main screen
            currentColor = (0, 127*(math.sin((self.cycle+i)/25) + 1), 255)
            pygame.draw.circle(temp, currentColor, (self.w/2, self.h/2), self.r-i)
        screen.blit(temp, (self.x, self.y))