import pygame

class HPBar(object):
    # Constructor for HP Bars that takes parameter of the entity's current health
    def __init__(self, hpamt):
        self.maxHp = hpamt
        self.hp = hpamt
        self.w = 10 * self.maxHp # define the width and height of the hp bar based on the initial hp
        self.h = 10
    
    # display the HP bar on screen at the set position, which in all cases if above entities' heads 
    def display(self, screen, centerX, centerY):
        if self.hp > 0:
            pygame.draw.rect(screen, (0, 0, 0), (centerX - self.w/2, centerY - self.h/2, self.w, self.h)) # draw a black background rectangle so the hp bar stands out
            pygame.draw.rect(screen, (255 - 255*(self.hp/self.maxHp), 255*(self.hp/self.maxHp), 0), (centerX - self.w/2 + 2, centerY - self.h/2 + 2, self.hp * (self.w - 4) / self.maxHp, self.h - 4)) # modulate color based on the amount of hp left vs. total hp, and draw a rectangle of the correct width