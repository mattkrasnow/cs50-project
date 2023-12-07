import pygame

class TextScreen(object):
    # Constructor that takes strings to be displayed and the window dimensions
    def __init__(self, textBlocks, screenwidth, screenheight):
        self.textItems = textBlocks # store inputted text
        self.frame = 0 # initialize frame sot he level can progress
        self.levelComplete = False # same variables as levels have, so no errors in main
        self.levelFailed = False
        self.enemyHit = False
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.spawnX = screenwidth/2
        self.spawnY = screenheight/2
    
    # Prevents calling a method that doesn't exist
    def populateEnemies(self):
        pass

    # Increases the time, makes the text move
    def levelPhysics(self, duck):
        self.frame += 1
        return False
    
    # Prevents calling a method that doesn't exist
    def bulletCollisions(self, bullet, damage):
        pass

    # Displays the text on screen, Star Wars Style
    def display(self, screen):
        yPos = self.screenheight - self.frame # sets the position of the top item
        for i in range(len(self.textItems)): # loop over the text items
            yStep = 18 + int((self.screenheight - self.frame + 20*i)/20) # step by a different amount depending on text size of the current block
            yPos += yStep # move the position of the text 
            
            font = pygame.font.Font('SourceCodePro-SemiBold.ttf', 40)
            text = font.render(self.textItems[i], True, (0,255,0), (50,50,50))
            scaleFactor = 1 - ((self.screenheight - yPos)/self.screenheight) # scale the text rectangle to make the effect of text scrolling
            if scaleFactor < 0:
                scaleFactor = 0 # don't allow negative scale factors
            text = pygame.transform.scale_by(text, scaleFactor) # scale the text
            aRect = text.get_rect()
            aRect.center = (self.screenwidth/2, yPos)
            screen.blit(text, aRect) # draw the text onto the screen in the correct position
        if yPos< 0:
            self.levelComplete = True # once all the text has left the screen, end the level