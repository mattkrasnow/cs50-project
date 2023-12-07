import random
from answer import Answer
from level import Level
from block import Block

class McQuestion():
    # Constructor for question "levels". Parameters: question asked to player, possible answers, the index of the correct answer, and the window dimensions
    def __init__ (self, question, answers, correctIndex, screenWidth, screenHeight):
        self.spawnX = screenWidth/2
        self.spawnY = 200
        blocks = [Block(0, screenHeight-350, 200, 20), Block(screenWidth - 200, screenHeight-350, 200, 20), Block(screenWidth/2 - 100, screenHeight-200, 200, 20), Block(screenWidth/2-200, screenHeight-50, 100, 20), Block(screenWidth/2+100, screenHeight-50, 100, 20)] # predefined blocks for question levels
        self.level = Level([], blocks, 100000, 100000, screenWidth, screenHeight, self.spawnX, self.spawnY, disptext=question) # create a level to run the physics and collisions of the multiple choice question, with no exit (off the screen), and displaying the text of the question
        positions = [[100, 150], [100, screenHeight-100], [screenWidth-100, 150], [screenWidth-100, screenHeight-100]]
        self.answers = []
        for i in range(4): # randomize the order of the answers
            ind = random.randint(0, 3-i)
            self.answers.append(Answer(answers[i], positions[ind][0], positions[ind][1], i == correctIndex)) # for each answer, add to the array of this level's answers a portal that is either correct or incorrect, and put it in a random unused position
            del positions[ind]
        self.levelComplete = False
        self.levelFailed = False
        self.enemyHit = False
        self.screenwidth = screenWidth
        self.screenheight = screenHeight
        self.questionAnswered = False

    # display the questions and answers on the screen
    def display(self, screen):
        self.level.display(screen) # draw the level in, which shows the blocks

        for a in self.answers:
            a.display(screen) # draw in each of the exits
    
    # define if the duck has answered the question correctly and duck's movement
    def levelPhysics(self, duck):
        self.level.levelPhysics(duck) # run the level physics with the stored level, which handles the player colliding with blocks
        for a in self.answers:
            if a.duckCollision(duck): # for every portal, check if the player is touching it
                if a.correctness: # if the player touches the correct portal, they complete the level, and return True, signaling to power up
                    self.levelComplete = True
                    if self.questionAnswered == False:
                        self.questionAnswered = True # only allow the player to get the power up once
                        return True
                else:
                    self.levelFailed = True # fail the level if the player chooses the wrong portal, which will move them back a level
                    self.questionAnswered = True # only allow the player to power up if they choose the correct answer on the first try
        return False
    
    # Prevents developer errors if the developer treats mcquestion objects as levels
    def bulletCollisions(self, bullets, damage):
        pass
    
    # Prevents developer errors if the developer treats mcquestion objects as levels
    def populateEnemies(self):
        pass