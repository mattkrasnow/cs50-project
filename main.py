import pygame
import sys

pygame.init()

LENGTH = 480
WIDTH = 640
BACKGROUND = (255,255,255)


# define aspects of the window
screen = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption('CS50 Duck to the Rescue')

# create the image of the duck
duckImg = pygame.image.load("cs50duck.png")
#duckImg = pygame.transform.scale(duckImg, )


# function to draw the duck
def duck(x,y):
    screen.blit(duckImg, (x,y) )


# set initial position of duck
xpos = (400)
ypos = (400)


run = True
while run:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    #draw the duck in the game
    screen.fill(BACKGROUND)
    duck(20,60)


    pygame.display.update()

pygame.quit()
sys.exit()