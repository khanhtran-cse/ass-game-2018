import pygame
import random
import time

from bullet import *
from menu import *
from score import *
from main import *

class OtherTank:
    # Image for rendering Tank
    shape = [
            pygame.image.load('./images/tank-move-up.png'),
        ]
    fire = (
        pygame.image.load('./images/tank-fire-0.png'),
        pygame.image.load('./images/tank-fire-1.png'),
        pygame.image.load('./images/tank-fire-2.png'),
        pygame.image.load('./images/tank-fire-3.png'),
        pygame.image.load('./images/tank-fire-4.png'),
    )

    shapeWidth,shapeHeight = shape[0].get_rect().size
    fireWidth,fireHeight = fire[0].get_rect().size
    
    # After the ``run`` function was called ``default_amination_speed`` times
    # the image source will be changed
    default_amination_speed = 1

    def __init__(self,gameDisplay,x,y):
        self.gameDisplay = gameDisplay
        self.x = x
        self.y = y
        self.deltaX = 2
        self.deltaY = 0
        self.isBug = False
        self.isCompleteMission = False
        self.isFailureMission = False
        self.fireShapeIndex = 0
        self.frameCount = 1
        self.animation_speed = OtherTank.default_amination_speed

    # Set speed for object
    def set_speed(self,deltaX, deltaY):
        self.deltaX = deltaX
        self.deltaY = deltaY

    # 1 loop, call 1 time
    # Draw the tank
    def draw(self):
        if self.isBug: 
            self.drawFire()
        if self.isCompleteMission or self.isFailureMission:
            return

        self.x += self.deltaX

        self.gameDisplay.blit(OtherTank.shape[0],(self.x,self.y))


        sw, sh = OtherTank.shape[0].get_rect().size
        w, h = pygame.display.get_surface().get_size()
        if self.x + sw > w - 50:
            self.finishMission()

    # Fire, it means the tank was destroyed
    # This function will draw destroyed animation
    def drawFire(self):
        if self.fireShapeIndex < 5:
            x = self.x + OtherTank.shapeWidth/2 - OtherTank.fireWidth/2
            y = self.y + OtherTank.shapeHeight/2 - OtherTank.fireHeight/2
            if self.frameCount < self.animation_speed:
                self.frameCount += 1
                self.gameDisplay.blit(OtherTank.fire[self.fireShapeIndex],(x,y))
            else:
                self.gameDisplay.blit(OtherTank.fire[self.fireShapeIndex],(x,y))
                self.fireShapeIndex += 1
                self.frameCount = 1
        else:
            self.isBug = False
    
    def finishMission(self):
        self.isBug = True
        self.isCompleteMission = True
        pygame.mixer.Sound('./sounds/failure.wav').play()

    def failureMission(self):
        self.isFailureMission = True
        self.isBug = True
        pygame.mixer.Sound('./sounds/fire.wav').play()

    # Determines that the tank is shoted or not
    def otherShotAt(self,position):
        if not self.isCompleteMission and not self.isFailureMission:
            x = position[0]
            y = position[1]
            if x > self.x and x < self.x + OtherTank.shapeWidth \
            and y > self.y and y < self.y + OtherTank.shapeHeight:
                self.failureMission()
                return True
            return False

    def isDestroy(self):
        if self.isBug:
            return False
        return self.isCompleteMission or self.isFailureMission
    
    # Get the mission result of the tank
    # If the tank completed missions, this function will return True, otherwise False
    def getMissionResult(self):
        return self.isCompleteMission
        


    # param ``fps``: the fps of the game
    # param ``speed``: the number shape frame was changed per second
    def set_animation_speed(self,fps, speed):
        if speed > 0 and fps > 0:
            self.animation_speed = fps/speed
            if self.animation_speed < OtherTank.default_amination_speed: 
                self.animation_speed = OtherTank.default_amination_speed
        else:
            self.animation_speed = OtherTank.default_amination_speed

class MyTank:

    # Image for rendering Jerry
    shape = [
            pygame.image.load('./images/my-tank-left.png'),
            pygame.image.load('./images/my-tank-right.png'),
            pygame.image.load('./images/my-tank-up.png'),
            pygame.image.load('./images/my-tank-down.png')
        ]
    def __init__(self,gamedisplay,x,y,id_tank,id_group):
        self.gamedisplay = gamedisplay
        self.x = x
        self.y = y
        self.id_tank = id_tank
        self.id_group = id_group

    def draw(self,positionImage):
        self.gamedisplay.blit(positionImage,(self.x,self.y))

    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
                self.y += -10
            elif event.key == pygame.K_DOWN:
                print("DOWN")
                self.y += 10
            elif event.key == pygame.K_LEFT:
                print("LEFT")
                self.x += -10
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                self.x += 10




