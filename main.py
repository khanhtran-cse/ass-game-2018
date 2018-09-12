import pygame
import random
import time

from tank import *
from score import *


# Define the size of the window
WINDOW_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 1050, 700


#Define some colors
WHITE = (255,255,255)
BLACK = (0,0,0)


def shotAt(tanks,position):
    for tank in tanks:
        if tank.otherShotAt(position):
        	score.increaseScore()
        	return
    else:
        score.decreaseMiss()



def removeDestroyTank(tanks, score):
    i = 0
    while i < len(tanks):
        if tanks[i].isDestroy():
        	print('Destroy a tank')
        	del tanks[i]
        	i -= 1
        i += 1

def createNewTank(tanks, gameDisplay):
    if len(tanks) < 5:
        y = random.randint(50,DISPLAY_HEIGHT-50)
        tank = OtherTank(gameDisplay,0,y)
        tank.set_animation_speed(FPS,30)
        tank.set_speed(random.randint(1,5),0)

        tanks.append(tank)



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

score = Score(gameDisplay, 5, 5);

# Init Jerry object
tanks = [
    OtherTank(gameDisplay,0,0),
    OtherTank(gameDisplay,200,200),
    OtherTank(gameDisplay,0,200),
    OtherTank(gameDisplay,0,400),
    OtherTank(gameDisplay,10,300)
]
for tank in tanks:
    tank.set_animation_speed(FPS,30)
    tank.set_speed(3,0)

# Init my tank
myTank = MyTank(gameDisplay,DISPLAY_WIDTH-100,0)
myTank.set_speed(4,8)

# This is used for defining fps for game.
# Ex: clock.tick(60) indicates that this game has fps is 60
clock = pygame.time.Clock()

finishedGame = False

while not finishedGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finishedGame = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if myTank.isReadyToShot():
                shotAt(tanks,pygame.mouse.get_pos())

    removeDestroyTank(tanks, score)
    createNewTank(tanks,gameDisplay)



    gameDisplay.blit(background,(0,0))
    score.draw()

    # pygame.draw.rect(gameDisplay,BLACK,pygame.Rect(0,300,DISPLAY_WIDTH,305))

    for tank in tanks:
        tank.draw()

    myTank.draw(pygame.mouse.get_pos())
    pygame.display.flip()

    # This will block execution until 1/60 seconds have passed 
    # since the previous time clock.tick was called.
    clock.tick(FPS)

pygame.quit()
quit()
