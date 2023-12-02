import pygame
import sys
from duck import Duck
from block import Block
from enemy import Enemy
from bullet import Bullet
from level import Level

pygame.init()

HEIGHT = 600
WIDTH = 800
BACKGROUND = (255,255,255)
btime = 15



# define aspects of the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CS50 Duck to the Rescue')

# intialize duck
duck = Duck(400, 600, WIDTH, HEIGHT)
clock = pygame.time.Clock()
level = Level([Enemy(400, 300, WIDTH, HEIGHT), Enemy(200, 300, WIDTH, HEIGHT)], [Block(0, 500, 200, 30), Block(400, 300, 100, 20), Block(200, 400, 100, 10)], 700, 500, WIDTH, HEIGHT)
run = True
bullets = []
while run:
    clock.tick(60)
    duck.move()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    #draw the duck in the game
    screen.fill(BACKGROUND)
    duck.display(screen)
    duck.jumping = True
    level.levelPhysics(duck)
    level.display(screen)


    #draw a bullet at the location of the duck
    if btime < 15:
        btime += 1
    if pygame.key.get_pressed()[pygame.K_SPACE] and btime == 15:
        btime = 0
        bullets.append(Bullet(duck.x+duck.w/2, duck.y+duck.h/2, duck.dir))
        
    for bullet in bullets:
        bullet.display(screen)
        bullet.move()

    pygame.display.update()

pygame.quit()
sys.exit()