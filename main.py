import pygame
import sys
import cv2
from duck import Duck

pygame.init()

HEIGHT = 1080
WIDTH = 1920
BACKGROUND = (255,255,255)


# define aspects of the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CS50 Duck to the Rescue')

# intialize duck
duck = Duck(400, 1080)
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    if duck.y >= 1080 - duck.h:
        duck.y = 1080 - duck.h
        duck.jumping = False

    duck.move()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    #draw the duck in the game
    screen.fill(BACKGROUND)
    duck.draw(screen)


    pygame.display.update()

pygame.quit()
sys.exit()