import pygame
import random
import time

# Define the size of the window
WINDOW_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 1000, 700

# Define the fps
FPS = 60

#Define some colors
WHITE = (255,255,255)
BLACK = (0,0,0)

class Jerry:
    # Image for rendering Jerry
    shape = [
            pygame.image.load('./images/jerry-run-1.png'),
            pygame.image.load('./images/jerry-run-2.png'),
            pygame.image.load('./images/jerry-run-3.png'),
            pygame.image.load('./images/jerry-run-4.png')
        ]
    
    # After the ``run`` function was called ``default_amination_speed`` times
    # the image source will be changed
    default_amination_speed = 1

    def __init__(self,gameDisplay,x,y):
        self.gameDisplay = gameDisplay
        self.shapeIndex = 0
        self.animation_speed = Jerry.default_amination_speed
        self.runCount = Jerry.default_amination_speed
        self.x = x
        self.y = y
        self.delta_x = 2
        self.delta_y = 0

    # 1 loop, call 1 time
    def run(self):
        self.x += self.delta_x
        self.y += self.delta_y
        self.gameDisplay.blit(Jerry.shape[self.shapeIndex],(self.x,self.y))

        sw, sh = Jerry.shape[self.shapeIndex].get_rect().size
        w, h = pygame.display.get_surface().get_size()
        if self.x + sw > w: self.delta_x = -2
        elif self.x < 0: self.delta_x = 2

        if self.y + sh > h: self.delta_y = 0
        elif self.y < 0: self.delta_y = 0

        if self.runCount > 0:
            self.runCount-=1
            return

        self.shapeIndex+=1
        if(self.shapeIndex >= 4): self.shapeIndex = 0
        self.runCount = self.animation_speed

    # param ``fps``: the fps of the game
    # param ``speed``: the number shape frame was changed per second
    def set_animation_speed(self,fps, speed):
        if speed > 0 and fps > 0:
            self.animation_speed = fps/speed
            if self.animation_speed < Jerry.default_amination_speed: 
                self.animation_speed = Jerry.default_amination_speed
        else:
            self.animation_speed = Jerry.default_amination_speed

# Initilize python
pygame.init()

# Set the size for the window
gameDisplay = pygame.display.set_mode(WINDOW_SIZE)

# Set caption for the window
pygame.display.set_caption('Tom And Jerry')

# Init Jerry object
jerry1 = Jerry(gameDisplay,0,0)
jerry1.set_animation_speed(FPS,10)


# Init Jerry object
jerry2 = Jerry(gameDisplay,200,200)
jerry2.set_animation_speed(FPS,10)


jerry3 = Jerry(gameDisplay,0,200)
jerry3.set_animation_speed(FPS,10)


jerry4 = Jerry(gameDisplay,0,400)
jerry4.set_animation_speed(FPS,20)


jerry5 = Jerry(gameDisplay,10,300)
jerry5.set_animation_speed(FPS,30)

# This is used for defining fps for game.
# Ex: clock.tick(60) indicates that this game has fps is 60
clock = pygame.time.Clock()

finishedGame = False

while not finishedGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finishedGame = True

    gameDisplay.fill(WHITE)
    # pygame.draw.rect(gameDisplay,BLACK,pygame.Rect(0,300,DISPLAY_WIDTH,305))

    jerry1.run()
    jerry2.run()
    
    jerry5.run()
    
    jerry4.run()
    
    jerry3.run()
    pygame.display.flip()

    # This will block execution until 1/60 seconds have passed 
    # since the previous time clock.tick was called.
    clock.tick(FPS)

pygame.quit()
quit()
