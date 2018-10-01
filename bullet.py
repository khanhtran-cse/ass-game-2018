import pygame

class Bullet:

    bullet = [
            pygame.image.load("./images/bullet-left.png"),
            pygame.image.load("./images/bullet-right.png"),
            pygame.image.load("./images/bullet-up.png"),
            pygame.image.load("./images/bullet-down.png")
    ]

    list = [5,4,3,2,1]

    def __init__(self,gameDisplay,id_tank,id_group,speed,x_start,y_start,x_end,y_end):
        self.gameDisplay = gameDisplay
        self.id = id_tank
        self.id_group = id_group
        self.speed = speed
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end

    def draw(self,positionBullet):
        self.gameDisplay.blit(positionBullet,(self.x_start,self.y_start))

    def motion(self,event,positionBullet):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        self.speed = 10
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_SPACE:
            #         self.speed = 0
                    #print(self.speed)
            return self.speed

    def colision_Bullet(self):
        pass






















