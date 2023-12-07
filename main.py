import pygame
import sys
from duck import Duck
from block import Block
from enemy import Enemy
from bullet import Bullet
from level import Level
from mcquestion import McQuestion
from boss import Boss
import math
from textscreen import TextScreen

pygame.init()


BACKGROUND = (50,50,50)
btime = 15
hitCooldown = 60
hp = 10
bulletDamage = 1



# define aspects of the window
screen = pygame.display.set_mode((960, 600))
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption('CS50 Duck to the Rescue')

# intialize duck
duck = Duck(0, HEIGHT-150, WIDTH, HEIGHT)
clock = pygame.time.Clock()
levels = [
    TextScreen(['The Year is 2024...', "it is set to be CS50's biggest yet", 'But there is one problem', 'The evil coders at MIT have hacked the code!', 'In all the chaos, only one man can save CS50', 'Or, as it would be, one duck.'], WIDTH, HEIGHT),
    TextScreen(['After hacking into the MIT mainframe,', 'the duck discovers something sinister...', 'It is a maze filled with evil beavers!', 'He must reach the portals on each level', 'Defeat the beavers,', 'and answer questions to save the psets!'], WIDTH, HEIGHT),
    Level([], [Block(500, HEIGHT - 100, 20, 100)], 900, 500, WIDTH, HEIGHT, 100, 400, disptext="Use the A and D keys to move around the level, and the W key to jump!"),
    Level([[750, HEIGHT - 400]], [Block(500, HEIGHT - 100, 300, 20), Block(800, HEIGHT - 200, 100, 20)], 850, HEIGHT - 400, WIDTH, HEIGHT, 100, 400, disptext="Click to shoot at evil beavers, and don't get hit!"),
    Level([], [], 850, HEIGHT - 100, WIDTH, HEIGHT, 100, 400, disptext="To recover each pset, you must answer a question correctly. Getting it right on the first try increases your damage!"),
    McQuestion('In Scratch, what is the purpose of a loop?', ['Drawing a circle', 'Repeating code', 'Moving in a circle', 'There are no loops'], 1, WIDTH, HEIGHT),
    Level([[750, HEIGHT - 400], [700, HEIGHT - 400], [650, HEIGHT - 400], [600, HEIGHT - 400]], [Block(200, HEIGHT - 200, WIDTH - 200, 20), Block(0, HEIGHT - 100, 50, 20)], 850, HEIGHT - 400, WIDTH, HEIGHT, 100, 400, disptext="The MIT beavers aren't that smart, so try to take advantage!"),
    McQuestion('Which is the correct header for a loop in c?', ['for(i = 0, i < 5; i++)', 'for(int i = 0; i < 5; i++)', 'do while():', 'for i in range(5)'], 1, WIDTH, HEIGHT),
    Level([[750, HEIGHT - 200], [700, HEIGHT - 200]], [Block(0, HEIGHT - 200, 200, 20), Block(200, HEIGHT - 150, 200, 20), Block(400, HEIGHT - 100, 200, 20), Block(600, HEIGHT - 50, 200, 20)], 850, HEIGHT - 150, WIDTH, HEIGHT, 0, 200, disptext="Be careful, the beavers can jump too!"),
    McQuestion('Which is NOT a property of arrays in c?', ['Stores a list of items', 'Stores a single type', 'Has dynamic size', 'Can be multidimensional'], 2, WIDTH, HEIGHT),
    Level([[0, 50], [700, 50], [0, HEIGHT - 150], [700, HEIGHT - 150]], [Block(0, 200, 200, 20), Block(WIDTH - 200, 200, 200, 20), Block(WIDTH/2 - 100, HEIGHT - 200, 200, 20)], 900, HEIGHT - 200, WIDTH, HEIGHT, WIDTH/2-75, HEIGHT - 550, disptext="Don't fall down!"),
    McQuestion('Of the following, which is the slowest sorting algorithm?', ['QuickSort', 'MergeSort', 'BubbleSort', 'InsertionSort'], 2, WIDTH, HEIGHT),
    Level([[0, HEIGHT - 150*i] for i in range(10)], [Block(0, HEIGHT - 150 * i + 100, 50, 20) for i in range(10)], 900, HEIGHT - 200, WIDTH, HEIGHT, 250, HEIGHT - 150, disptext="Run!"),
    McQuestion('Which piece of code should always follow a malloc() call?', ['calloc()', 'free()', 'A pointer', 'The stack'], 1, WIDTH, HEIGHT),
    Level([[450 + 50 * i, HEIGHT - 150] for i in range(8)], [], 900, HEIGHT - 200, WIDTH, HEIGHT, 0, HEIGHT - 150, disptext="Hope you have enough damage!"),
    McQuestion('In which case would a linked list be better than an array?',  ['List of constant length', 'Limited available memory', 'List of unknown length', 'Never'], 2, WIDTH, HEIGHT),
    Level([], [Block(150 + 100 * i, HEIGHT - 50 * i, 80, 20) for i in range(8)], 900, 100, WIDTH, HEIGHT, 0, HEIGHT - 150, disptext="Here's a little break."),
    McQuestion('What terminal command opens the database fiftyville.db?', ['sqlite3 fiftyville.db', 'SELECT * FROM users', 'import sqlite3 from Python', 'SELECT * FROM fiftyville.db'], 0, WIDTH, HEIGHT),
    Level([[WIDTH/2, HEIGHT - 100], [WIDTH/2, HEIGHT - 250], [WIDTH/2, HEIGHT - 400], [WIDTH/2, HEIGHT - 550]], [Block(0, HEIGHT - 150, WIDTH - 100, 20), Block(100, HEIGHT - 300, WIDTH - 100, 20), Block(0, HEIGHT - 450, WIDTH - 100, 20)], 80, 60, WIDTH, HEIGHT, 0, HEIGHT - 150, disptext="The duck is climbing higher, sensing something coming soon!"),
    McQuestion('How can static websites change?', ['The developer changes the code', 'The user interacts with the display', 'They cannot be changed', 'They can be changed by many factors'], 0, WIDTH, HEIGHT),
    Level([], [], 900, HEIGHT - 150, WIDTH, HEIGHT, 0, HEIGHT - 150, "The duck slows down. It knows the next question is the last pset"),
    McQuestion('What is NOT a language used when using Flask?', ['JavaScript', 'HTML', 'CSS', 'C'], 3, WIDTH, HEIGHT),
    TextScreen(['The duck breathes heavily.', 'It knows it has finished all the psets,', 'but it still feels like something is missing.', 'It hears some sounds from just a little further,', 'and realizes what he forgot about.', 'The final project!', 'Somehow, MIT has captured all the old final projects,', 'and placed its strongest beaver to protect them.', "This will be the duck's hardest battle yet", 'Good luck.'], WIDTH, HEIGHT),
    Boss(WIDTH, HEIGHT),
    TextScreen(["Congratulations, you have saved CS50!", "With the beavers defeated,", "The duck recovers the rest of the code", "He rushes home and puts it in place,", "starting codespaces minutes before Lecture 0.", "CS50 is saved!"], WIDTH, HEIGHT)
]
run = True
bullets = []
currentLevel = 0
while run:
    if levels[currentLevel].levelComplete:
        currentLevel += 1
        levels[currentLevel].levelComplete = False
        levels[currentLevel].levelFailed = False
        duck.x = levels[currentLevel].spawnX
        duck.y = levels[currentLevel].spawnY
        duck.yvel = 0
        duck.vel = 0
    if levels[currentLevel].levelFailed:
        currentLevel -= 1
        levels[currentLevel].levelComplete = False
        levels[currentLevel].levelFailed = False
        duck.x = levels[currentLevel].spawnX
        duck.y = levels[currentLevel].spawnY
        levels[currentLevel].populateEnemies()
        duck.yvel = 0
        duck.vel = 0
    clock.tick(60)
    duck.move()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    #draw the duck in the game
    screen.fill(BACKGROUND)
    
    duck.jumping = True
    firstRight = levels[currentLevel].levelPhysics(duck)
    if firstRight:
        bulletDamage += 1
    
    levels[currentLevel].display(screen)

    levels[currentLevel].bulletCollisions(bullets, bulletDamage)


    #draw a bullet at the location of the duck
    if btime < 30:
        btime += 1
    if pygame.mouse.get_pressed()[0] and btime == 30:
        btime = 0
        bulletX = duck.guntipX
        bulletY = duck.guntipY
        mX, mY = pygame.mouse.get_pos()
        xDiff = mX - bulletX
        yDiff = mY - bulletY
        normFactor = math.sqrt(xDiff * xDiff + yDiff * yDiff)
        xDiff = 8 * xDiff / normFactor
        yDiff = 8 * yDiff / normFactor
        bullets.append(Bullet(bulletX, bulletY, xDiff, yDiff))

    if hitCooldown < 60:
        hitCooldown += 1
    if levels[currentLevel].enemyHit and hitCooldown == 60:
        hitCooldown = 0
        hp -= 1
        duck.hp = hp
        if levels[currentLevel].hitDirection == 'r':
            duck.jumping = True
            duck.y -= 8
            duck.yvel += 5
            duck.vel = 5
        else:
            duck.jumping = True
            duck.y -= 8
            duck.yvel += 5
            duck.vel = -5
        if hp == 0:
            bulletDamage = 1
            currentLevel = 0
            levels[currentLevel].levelComplete = False
            hp = 10
            duck.hp = hp
            levels[currentLevel].populateEnemies()
            duck.vel = 0
            duck.yvel = 0
            duck.x = levels[currentLevel].spawnX
            duck.y = levels[currentLevel].spawnY
        
    for bullet in bullets:
        bullet.display(screen)
        bullet.move()
        if bullet.x < -100 or bullet.x > WIDTH + 100 or bullet.y < -100 or bullet.y > HEIGHT + 100:
            bullets.pop(bullets.index(bullet))
    duck.display(screen)

    pygame.display.update()

pygame.quit()
sys.exit()