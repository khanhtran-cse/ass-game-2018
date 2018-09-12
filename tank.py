import pygame
import random
import time

# Define the fps
FPS = 60


# Define the size of the window
WINDOW_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 1050, 700

class OtherTank:
    # Image for rendering Tank
    shape = [
            pygame.image.load('./images/tank-move-right.png'),
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
            pygame.image.load('./images/my-tank.png'),
        ]
    notReadyIcon = pygame.image.load('./images/not-ready.png')
    shotIcon = pygame.image.load('./images/cursor-shot.png')
  
    def __init__(self,gameDisplay,x,y):
        self.gameDisplay = gameDisplay
        self.x = x
        self.y = y
        self.deltaX = 2
        self.deltaY = 2
        self.isMovedToMouse = False

    # Set speed for object
    def set_speed(self,deltaX, deltaY):
        self.deltaX = deltaX
        self.deltaY = deltaY

    # 1 loop, call 1 time
    def draw(self, position):
        # Get the size of the shape
        shapeWidth, shapeHeight = MyTank.shape[0].get_rect().size

        # Get the middle point of the shape
        middleY = self.y + shapeHeight/2

        # new position
        if middleY < position[1]:
            middleY += self.deltaY
            if middleY >= position[1]:
                middleY = position[1]
                self.isMovedToMouse = True
            else:
                self.isMovedToMouse = False

        elif middleY > position[1]:
            middleY -= self.deltaY
            if middleY <= position[1]:
                middleY = position[1]
                self.isMovedToMouse = True
            else:
                self.isMovedToMouse = False
        
        
        # Detemine weather the tank is at the edge or not 
        # w, h = pygame.display.get_surface().get_size()
        self.y = middleY - shapeHeight/2
        # if self.y < 0:
        #     self.y = 0
        # elif self.y > h - shapeHeight:
        #     self.y = h - shapeHeight

        # draw Tank into game display
        self.gameDisplay.blit(MyTank.shape[0],(self.x,self.y))

        cursorX = position[0] -12
        cursorY = position[1] - 12
        if cursorX < 0: 
            cursorX = 0
        if cursorY < 0:
            cursorY = 0

        if self.isMovedToMouse:
            self.gameDisplay.blit(MyTank.shotIcon,(cursorX,cursorY))
        else:
            self.gameDisplay.blit(MyTank.notReadyIcon,(cursorX,cursorY))
    def isReadyToShot(self):
        return self.isMovedToMouse
