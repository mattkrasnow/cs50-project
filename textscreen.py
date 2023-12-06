import pygame

class TextScreen(object):
    def __init__(self, textBlocks, screenwidth, screenheight):
        self.textItems = textBlocks
        self.frame = 0
        self.levelComplete = False
        self.levelFailed = False
        self.enemyHit = False
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.spawnX = screenwidth/2
        self.spawnY = screenheight/2
    
    def populateEnemies(self):
        pass

    def levelPhysics(self, duck):
        self.frame += 1
        return False
    
    def bulletCollisions(self, bullet, damage):
        pass

    def display(self, screen):
        yPos = self.screenheight - self.frame
        for i in range(len(self.textItems)):
            yStep = 18 + int((self.screenheight - self.frame + 20*i)/20)
            yPos += yStep
            if yPos + yStep < 0:
                self.levelComplete = True
            font = pygame.font.Font('SourceCodePro-SemiBold.ttf', 40)
            text = font.render(self.textItems[i], True, (0,255,0), (50,50,50))
            scaleFactor = 1 - ((self.screenheight - yPos)/self.screenheight)
            if scaleFactor < 0:
                scaleFactor = 0
            text = pygame.transform.scale_by(text, scaleFactor)
            aRect = text.get_rect()
            aRect.center = (self.screenwidth/2, yPos)
            screen.blit(text, aRect)