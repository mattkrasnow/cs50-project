import pygame
import sys
from duck import Duck
from block import Block
from enemy import Enemy
from bullet import Bullet

pygame.init()

HEIGHT = 600
WIDTH = 800
BACKGROUND = (255,255,255)


# define aspects of the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CS50 Duck to the Rescue')

# intialize duck
duck = Duck(400, 600, WIDTH, HEIGHT)
clock = pygame.time.Clock()
currentLevelBlocks = [Block(0, 500, 200, 30), Block(400, 300, 100, 20)]
enemies = [Enemy(400, 300, WIDTH, HEIGHT)]
level = 0
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
    for block in currentLevelBlocks:
       block.objectCollision(duck)
       block.display(screen)
    for enemy in enemies:
        if enemy.y >= HEIGHT - enemy.h:
            enemy.y = HEIGHT - enemy.h
            enemy.jumping = False
        enemy.move(duck)
        enemy.display(screen)
        enemy.jumping = True   
        for block in currentLevelBlocks:
            block.objectCollision(enemy)


    #draw a bullet at the location of the duck
    btime = 15
    if btime < 15:
        btime += 1
    if pygame.key.get_pressed()[pygame.K_SPACE] and btime == 15:
        btime = 0
        bullets.append(Bullet(duck.x, duck.y, duck.dir))
        
    for bullet in bullets:
        bullet.display(screen)
        bullet.move()

    pygame.display.update()

pygame.quit()
sys.exit()