import pygame
import random
import time

from tank import *
from score import *


# Define the size of the window
WINDOW_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 1050, 700

# Define max miss
MAX_MISS = 10

#Define some colors
WHITE = (255,255,255)
BLACK = (0,0,0)

def shotAt(tanks,position):
    for tank in tanks:
        tank.otherShotAt(position)

def calculateScoreAndRemoveDestroyTank(tanks, score):
    i = 0
    while i < len(tanks):
        if tanks[i].isDestroy():
            if tanks[i].getMissionResult():
                score.decreaseMiss()
            else:
                score.increaseScore()
            del tanks[i]
            i -= 1
        i += 1

def createNewTank(tanks, maxTank, gameDisplay):
    if len(tanks) < maxTank:
        y = random.randint(50,DISPLAY_HEIGHT-50)
        tank = OtherTank(gameDisplay,0,y)
        tank.set_animation_speed(FPS,30)
        tank.set_speed(random.randint(1,5),0)

        tanks.append(tank)

# Invokes when game over
# Draw game over menu
def showGameOverMenu(gameDisplay,score):
    print('Game over')

# Initilize python
pygame.init()

# Set the size for the window
gameDisplay = pygame.display.set_mode(WINDOW_SIZE)

# Set caption for the window
pygame.display.set_caption('Tom And Jerry')

# Load background
background = pygame.image.load('./images/background.png')

# Hide cursor
pygame.mouse.set_visible(False)

# Play background sound
pygame.mixer.Sound('./sounds/background.wav').play(-1)

score = Score(gameDisplay, 15, 10)

# Init Enemy Tank array
tanks = []

# Init my tank
myTank = MyTank(gameDisplay,DISPLAY_WIDTH-100,0)
myTank.set_speed(4,8)

# This is used for defining fps for game.
# Ex: clock.tick(60) indicates that this game has fps is 60
clock = pygame.time.Clock()

gameOver = False
finishedGame = False

# To restart game, set this to True
restartGame = False

while not finishedGame:
    # Handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finishedGame = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if gameOver:
                restartGame = True
            else:
                if myTank.isReadyToShot():
                    shotAt(tanks,pygame.mouse.get_pos())

    # Reset state to start new game
    if restartGame:
        tanks = []
        score.resetScore()
        gameOver = False
        restartGame = False

    if score.getMiss() >= MAX_MISS:
        gameOver = True

    # Handle game over
    if gameOver:
        # Todo: Draw game over menu
        showGameOverMenu(gameDisplay,score)
        # This will block execution until 1/60 seconds have passed 
        # since the previous time clock.tick was called.
        clock.tick(FPS)
        continue

    # Calculate score and remove the tanks was shoted or the tanks was finished mission.
    calculateScoreAndRemoveDestroyTank(tanks, score)

    # Create new tanks to replace for the destroyed tanks
    # and inscrease the number of the tanks to increase difficult level
    maxTank = score.getScore()/10 + 4
    createNewTank(tanks,maxTank,gameDisplay)

    # Draw background to remove old state
    gameDisplay.blit(background,(0,0))

    # Draw score
    score.draw()

    # Draw enemy tanks
    for tank in tanks:
        tank.draw()

    # Draw my tank
    myTank.draw(pygame.mouse.get_pos())

    # Update the display
    pygame.display.flip()

    # This will block execution until 1/60 seconds have passed 
    # since the previous time clock.tick was called.
    clock.tick(FPS)

pygame.quit()
quit()
