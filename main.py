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

# set the variables used in main
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
# initialize the clock that keeps game speed consistent
clock = pygame.time.Clock()
# create the array of levels and level-like objects that is iterated through to run the game 
levels = [
    TextScreen(['The Year is 2024...', "it is set to be CS50's biggest yet", 'But there is one problem', 'The evil coders at MIT have hacked the code!', 'In all the chaos, only one man can save CS50', 'Or, as it would be, one duck.',
                '', '', '',
                'After hacking into the MIT mainframe,', 'the duck discovers something sinister...', 'It is a maze filled with evil beavers!', 'He must reach the portals on each level', 'Defeat the beavers,', 'and answer questions to save the psets!'], WIDTH, HEIGHT), # TextScreen objects take in a list of strings to make a Star-Wars-like scrolling text screen 
    Level([], [Block(500, HEIGHT - 100, 50, 100)], 900, 500, WIDTH, HEIGHT, 100, 400, disptext="Use the A and D keys to move around the level, and the W key to jump!"), # each level takes an array of enemy position, block positions, a player spawn point, and the location of an exit portal, as well as text to display
    Level([[750, HEIGHT - 400]], [Block(500, HEIGHT - 100, 300, 20), Block(800, HEIGHT - 200, 100, 20)], 850, HEIGHT - 400, WIDTH, HEIGHT, 100, 400, disptext="Click to shoot at evil beavers, and don't get hit!"),
    Level([], [], 850, HEIGHT - 100, WIDTH, HEIGHT, 100, 400, disptext="To recover each pset, you must answer a question correctly. Getting it right on the first try increases your damage!"),
    McQuestion('In Scratch, what is the purpose of a loop?', ['Drawing a circle', 'Repeating code', 'Moving in a circle', 'There are no loops'], 1, WIDTH, HEIGHT), # question levels take in a question, a list of answers, and the index of the correct answer
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
    Level([], [Block(150 + 100 * i, HEIGHT - 50 * i, 80, 20) for i in range(1, 8)], 900, 100, WIDTH, HEIGHT, 0, HEIGHT - 150, disptext="Here's a little break."),
    McQuestion('What terminal command opens the database fiftyville.db?', ['sqlite3 fiftyville.db', 'SELECT * FROM users', 'import sqlite3 from Python', 'SELECT * FROM fiftyville.db'], 0, WIDTH, HEIGHT),
    Level([[WIDTH/2, HEIGHT - 100], [WIDTH/2, HEIGHT - 250], [WIDTH/2, HEIGHT - 400], [WIDTH/2, HEIGHT - 550]], [Block(0, HEIGHT - 150, WIDTH - 100, 20), Block(100, HEIGHT - 300, WIDTH - 100, 20), Block(0, HEIGHT - 450, WIDTH - 100, 20)], 80, 60, WIDTH, HEIGHT, 0, HEIGHT - 150, disptext="The duck is climbing higher, sensing something coming soon!"),
    McQuestion('How can static websites change?', ['The developer changes the code', 'The user interacts with the display', 'They cannot be changed', 'They can be changed by many factors'], 0, WIDTH, HEIGHT),
    Level([], [], 900, HEIGHT - 150, WIDTH, HEIGHT, 0, HEIGHT - 150, "The duck slows down. It knows the next question is the last pset"),
    McQuestion('What is NOT a language used when using Flask?', ['JavaScript', 'HTML', 'CSS', 'C'], 3, WIDTH, HEIGHT),
    TextScreen(['The duck breathes heavily.', 'It knows it has finished all the psets,', 'but it still feels like something is missing.', 'It hears some sounds from just a little further,', 'and realizes what he forgot about.', 'The final project!', 'Somehow, MIT has captured all the old final projects,', 'and placed its strongest beaver to protect them.', "This will be the duck's hardest battle yet", 'Good luck.'], WIDTH, HEIGHT),
    Boss(WIDTH, HEIGHT), # the boss level is the same each time, with some randomness in the constructor. It doesn't need any inputs other than the screen dimensions, which all levels use
    TextScreen(["Congratulations, you have saved CS50!", "With the beavers defeated,", "The duck recovers the rest of the code", "He rushes home and puts it in place,", "starting codespaces minutes before Lecture 0.", "CS50 is saved!"], WIDTH, HEIGHT)
]

bullets = []
run = True
currentLevel = 0 # keep track of which index of the levels in the array the player is currently on
while run:
    if levels[currentLevel].levelComplete: # check for level completion conditions (touching the portal, or the scrolling text finishing)
        currentLevel += 1 # increment the next level, reset all of its variables to the default values in case the player has tried the level before, and put the duck in the correct spawn position. Finally, the level's enemies are repopulated
        if currentLevel == len(levels):
            run = False
            pygame.quit()
            sys.exit()
        levels[currentLevel].levelComplete = False
        levels[currentLevel].levelFailed = False
        duck.x = levels[currentLevel].spawnX
        duck.y = levels[currentLevel].spawnY
        duck.yvel = 0
        duck.vel = 0
        levels[currentLevel].populateEnemies()
    if levels[currentLevel].levelFailed: # check if the level is failed (this only happens when the player chooses the wrong gate on a question)
        currentLevel -= 1 # decrement the level, and reset all of its variables to the default values, as well as repopulating any enemies that were on the level. This ensures that there will be the proper amount of enemies on the level.
        levels[currentLevel].levelComplete = False
        levels[currentLevel].levelFailed = False
        duck.x = levels[currentLevel].spawnX
        duck.y = levels[currentLevel].spawnY
        levels[currentLevel].populateEnemies()
        duck.yvel = 0
        duck.vel = 0
    clock.tick(60) # this makes the game loop run at a consistent 60 frames per second. 
    duck.move() # call the duck movement, which takes player controls and updates the duck's position with their input and gravity. 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # if the player manually closes the game, pygame ends the loop.
   
    screen.fill(BACKGROUND) # fill in the background with our predefined color
    
    duck.jumping = True
    firstRight = levels[currentLevel].levelPhysics(duck) # runs the level physics on the duck. In most cases, this will return false and calculate block collisions, enemy collisions, portal collisions, and more depending on the level type.
    if firstRight: # if the function returns true, which only happens if the player gets a question right on their first try, their gun will gain more damage.
        bulletDamage += 1
    
    levels[currentLevel].display(screen) # displays the levels, which includes blocks, portals, and enemies. In the boss level, this also draws the boss. 

    levels[currentLevel].bulletCollisions(bullets, bulletDamage) # calculates bullet collisions with enemeis and bosses depending on the level type.v


    # increment timer for between bullet shots
    if btime < 30:
        btime += 1

    if pygame.mouse.get_pressed()[0] and btime == 30: # check if player is trying to shoot, and if they have waited enough time
        btime = 0
        bulletX = duck.guntipX
        bulletY = duck.guntipY
        mX, mY = pygame.mouse.get_pos() # get mouse position
        xDiff = mX - bulletX
        yDiff = mY - bulletY
        normFactor = math.sqrt(xDiff * xDiff + yDiff * yDiff) # normalize difference between mouse position and bullet so it moves at the same velocity in any direction
        xDiff = 8 * xDiff / normFactor
        yDiff = 8 * yDiff / normFactor
        bullets.append(Bullet(bulletX, bulletY, xDiff, yDiff)) # add a bullet to our list of bullets

    if hitCooldown < 60: # increment timer between times player can be hit
        hitCooldown += 1
    if levels[currentLevel].enemyHit and hitCooldown == 60: # if the enemy is currently hitting the player, and the player is able to be hit currently, the player loses some hp
        hitCooldown = 0
        hp -= 1
        duck.hp = hp
        if levels[currentLevel].hitDirection == 'r': # check what direction the hit came from. Move the player away and bounce off the ground a little bit
            duck.jumping = True
            duck.y -= 8
            duck.yvel += 5
            duck.vel = 5
        else:
            duck.jumping = True
            duck.y -= 8
            duck.yvel += 5
            duck.vel = -5
        if hp == 0: # if the player is out of HP, reset to the first level, and reset the player bullet damage as well. Since text scroller clock is not reset, those levels will not appear again
            bulletDamage = 1
            currentLevel = 0
            levels[currentLevel].levelComplete = False # additionally, run all the same level reset as when advancing one level or moving back one level
            hp = 10
            duck.hp = hp
            levels[currentLevel].populateEnemies() 
            duck.vel = 0
            duck.yvel = 0
            duck.x = levels[currentLevel].spawnX
            duck.y = levels[currentLevel].spawnY
        
    for bullet in bullets: # display and move each bullet. Additionally, check if it has moved off the screen, and if so, delete it
        bullet.display(screen)
        bullet.move()
        if bullet.x < -100 or bullet.x > WIDTH + 100 or bullet.y < -100 or bullet.y > HEIGHT + 100:
            bullets.pop(bullets.index(bullet))
    duck.display(screen) # draw the duck onto the screen

    pygame.display.update() # update the display so the player sees everything drawn this loop. 

pygame.quit() # exit pygame and end the code
sys.exit()