import pygame
from block import Block
from enemy import Enemy
from answer import Answer


class Level(object):
    # Constructor for level objects that takes parameters of the enemy starting positions, array of blocks in the level, position of exit portal, windo dimensions, the duck's spawn position, and any text displayed on screen
    def __init__(self, enemyPos, blocks, exitX, exitY, screenwidth, screenheight, spawnX, spawnY, disptext=""):
        self.enemyPos = enemyPos
        self.enemies = []
        self.blocks = blocks
        self.exit = Answer("", exitX, exitY, True) # define an empty answer with a value of True, so when the player collides with it, they will pass to the next level
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.levelComplete = False # initialize instance variables
        self.levelFailed = False
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.enemyHit = False
        self.hitDirection = 'r'
        self.text = disptext
        self.populateEnemies() # call populate enemeis to make the enemy array full with the correct enemies
    
    # Spawns in the enemies for the level at designated positions
    def populateEnemies(self):
        self.enemies = []
        for pos in self.enemyPos:
            self.enemies.append(Enemy(pos[0], pos[1], self.screenwidth, self.screenheight)) # add enemies to enemies array based on the positions passed into the constructor initially
    
    # Makes enemies move, block collisions with player/enemies, exit portal with the duck
    def levelPhysics(self, duck):
        for block in self.blocks:
            block.objectCollision(duck) # run all block physics with duck
        self.enemyHit = False
        for enemy in self.enemies:
            enemy.move(duck) # for every enemy, run its move method, which calculates its movement direction
            enemy.jumping = True   
            for block in self.blocks: # for every block, run the collision with each enemy so they all behave correctly with block collisions
                block.objectCollision(enemy)
            if enemy.duckCollision(duck): # as long the current enemy is colliding with the duck, we set enemyHit to true, signaling to main that the duck was hit. Additionally, set the hit direction so the duck bounces the right way. 
                self.enemyHit = True
                self.hitDirection = enemy.dir
        
        if(self.exit.duckCollision(duck)): # check if the duck is colliding with the exit, and if so, mark that the level is complete
            self.levelComplete = True 
        return False # return false, since this level is not a question, so the player can't power up their gun
        
    def bulletCollisions(self, bullets, damage):
        for enemy in self.enemies: 
            for bullet in bullets: # for every combination of enemy and bullet, we check if that bullet is hitting that enemy
                if bullet.enemyCollision(enemy):
                    enemy.hp -= damage # if the bullet is colliding with the enemy, we check its direction to bounce the enemy, and lower the enemy's hp
                    if bullet.xvel <= 0:
                        enemy.vel = -2
                    else:
                        enemy.vel = 2
                    enemy.yvel += 4
                    enemy.jumping = True
                    enemy.y -= 8
                    bullets.pop(bullets.index(bullet)) # once a bullet hits an enemy, remove it from the bullet array
                    if enemy.hp <= 0:
                        self.enemies.pop(self.enemies.index(enemy)) # if the enemy is out of hp, remove it from the enemy array
        
    # displays the  blocks and enemies on screen, text, and exit portal
    def display(self, screen):
        font = pygame.font.Font('SourceCodePro-SemiBold.ttf', 12)
        text = font.render(self.text, True,  (0,255,0), (50,50,50))
        aRect = text.get_rect()
        aRect.center = (self.screenwidth/2, 100)
        screen.blit(text, aRect) # center the text input in the constructor, and draw it on the top of the screen to display messages
        for block in self.blocks:
            block.display(screen) # draw all the blocks in the level
        for enemy in self.enemies:
            enemy.display(screen) # draw all the enemies in the level
        if not self.levelComplete:
            self.exit.display(screen) # draw the exit to the level