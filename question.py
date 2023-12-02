import pygame 
import time
import subprocess


HEIGHT = 600
WIDTH = 800
font = pygame.font.Font('freesansbold.ttf', 32)        


def write_to_file(filename, content):
    with open(filename, 'w') as f:
       f.write(content)


# give a textbox response for when the user inputs correct/incorrect information
def response(value):
    if value:
        text = font.render('Correct! Advancing level...', True, (0,255,0), (0,0,128))

    else:
        text = font.render('Incorrect! Resrarting level...', True, (0,255,0), (0,0,128))

    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    startTime = time.time()
    # display error message for 4 seconds then restart the level
    while time.time() - startTime < 4:
        display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        display_surface.fill((255,0,0))
        display_surface.blit(text, textRect)
    

# python syntax question
def syntaxQuestion(desiredResult):

    # ask the user for input on the screen
    answeredYet = False
    while not answeredYet:
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        text = font.render('Enter your python code:', True, (0,255,0), (0,0,128))
        display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        display_surface.fill((255,0,0))
        display_surface.blit(text, textRect)

        # CHANGE this to get input from the screen - Ask Max
        user_code = input("Enter your Python code: ")
   
    # Write the input to practice.py
    write_to_file('practice.py', user_code)
   
    # Now run practice.py
    try:
        # read the result from the terminal
        result = subprocess.run(subprocess.run(['python', 'practice.py']), shell=True, capture_output=True, text=True)
        if result == desiredResult:
            response(True)
        else:
            response(False)
        # TODO: Advance level
    except:
        response(False)
        # TODO: Restart level



if __name__ == "__main__":
    syntaxQuestion()


