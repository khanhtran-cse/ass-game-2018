import pygame
import random
import time

from tank import *
from score import *
from bullet import *

# Define FPS
FPS = 160

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

# Invokes when game over
# Draw game over menu
def showGameOverMenu(gameDisplay,score,mousePosition,gameOverText,hintText, hintFont, GAME_OVER_MOUSE):
    # gameDisplay.blit(gameOverText, (445, 300))
    score = hintFont.render('Your Score: ' + str(score.getScore()), True, (244, 66, 66))
    gameDisplay.blit(score, (350, 280))
    gameDisplay.blit(hintText, (400, 380))

    # Draw mouse
    cursorX = mousePosition[0] -12
    cursorY = mousePosition[1] - 12
    if cursorX < 0: 
        cursorX = 0
    if cursorY < 0:
        cursorY = 0
    gameDisplay.blit(GAME_OVER_MOUSE,(cursorX,cursorY))


def startTank(gameDisplay):
    # Set caption for the window
    pygame.display.set_caption('Super Tank')

    # Load background
    background = pygame.image.load('./images/background.png')

    # Hide cursor
    pygame.mouse.set_visible(False)

    # Play background sound
    pygame.mixer.Sound('./sounds/background.wav').play(-1)

    # Init score
    score = Score(gameDisplay, 15, 10)
    score.setMaxMiss(MAX_MISS)

    #Game over mouse 
    GAME_OVER_MOUSE = pygame.image.load('./images/cursor-shot.png')

    # Init Enemy Tank array
    tanks = []



    # Initial my tank
    myTank = MyTank(gameDisplay,0,400,id_tank=1,id_group=1,speed_x=0,speed_y=0)
    # myTank1 = MyTank(gameDisplay, 0,0, id_tank=2, id_group=1)
    # myTank2 = MyTank(gameDisplay, 0, 0, id_tank=3, id_group=1)
    # myTank3 = MyTank(gameDisplay, 0, 0, id_tank=4, id_group=1)
    # myTank_List = [myTank, myTank1,myTank2,myTank3]

    #Initial enemy tanks
    enemyTank = MyTank(gameDisplay,DISPLAY_WIDTH-100,0,id_tank=1,id_group=0,speed_x=0,speed_y=0)
    enemyTank1 = MyTank(gameDisplay, DISPLAY_WIDTH - 100, 0, id_tank=2, id_group=0,speed_x=0,speed_y=0)
    enemyTank2 = MyTank(gameDisplay, DISPLAY_WIDTH - 100, 0, id_tank=3, id_group=0,speed_x=0,speed_y=0)
    enemyTank3 = MyTank(gameDisplay, DISPLAY_WIDTH - 100, 0, id_tank=4, id_group=0,speed_x=0,speed_y=0)
    enemyTank_List = [enemyTank,enemyTank1,enemyTank2,enemyTank3]


    # Initial bullet
    bullet = Bullet(gameDisplay, id_tank=1, id_group=1, speed=0, x_start=myTank.x, y_start=myTank.y, x_end=0, y_end=0)


    # This is used for defining fps for game.
    # Ex: clock.tick(60) indicates that this game has fps is 60
    clock = pygame.time.Clock()

    gameOver = False
    finishedGame = False

    # To restart game, set this to True
    restartGame = False

    # Test menu
    gameOverFont = pygame.font.SysFont("helvetica", 60)
    hintFont = pygame.font.SysFont("helvetica", 30)
    gameOverText = gameOverFont.render('Game Over', True, (244, 66, 66))
    hintText = hintFont.render('Click here to continue', True, (0,0,0))

    speed_bullet = 0
    speed_tank_x  = 0
    speed_tank_y = 0

    while not finishedGame:

        # Handle event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            speed_tank_x = myTank.move(event)[0]
            speed_tank_y = myTank.move(event)[1]

            # bullet
            speed_bullet = bullet.motion(event,bullet.bullet[0])

        bullet.x_start += speed_bullet

        myTank.x += speed_tank_x
        myTank.y += speed_tank_y

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
            # Draw background to remove old state
            gameDisplay.blit(background,(0,0))
            # Todo: Draw game over menu
            showGameOverMenu(gameDisplay,score,pygame.mouse.get_pos(),gameOverText,hintText, gameOverFont, GAME_OVER_MOUSE)

            # Update the display
            pygame.display.flip()
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
        # for tank in tanks:
        #     tank.draw()

        #Display my tank
        myTank.draw(myTank.shape[myTank.index_myTank])
        #myTank1.draw(myTank1.shape[0])

        #Display enemy tank
        enemyTank_List[0].draw(myTank.shape[0])

        bullet.draw(bullet.bullet[0])

        # Update the display
        pygame.display.flip()

        # This will block execution until 1/60 seconds have passed 
        # since the previous time clock.tick was called.
        clock.tick(FPS)