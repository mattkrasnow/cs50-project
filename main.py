import pygame
import sys
from duck import Duck
from block import Block

pygame.init()

HEIGHT = 600
WIDTH = 800
BACKGROUND = (255,255,255)


# define aspects of the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CS50 Duck to the Rescue')

# intialize duck
duck = Duck(400, 600)
clock = pygame.time.Clock()
currentLevelBlocks = [Block(0, 500, 200, 30), Block(400, 300, 100, 20)]
run = True
while run:
    clock.tick(60)
    if duck.y >= HEIGHT - duck.h:
        duck.y = HEIGHT - duck.h
        duck.jumping = False

    duck.move()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    #draw the duck in the game
    screen.fill(BACKGROUND)
    duck.display(screen)
    duck.jumping = True
    for block in currentLevelBlocks:
       block.duckCollision(duck)
       block.display(screen)

    pygame.display.update()

pygame.quit()
sys.exit()