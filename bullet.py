import pygame

class Bullet:

    bullet = [
            pygame.image.load("./images/bullet-left.png"),
            pygame.image.load("./images/bullet-right.png"),
            pygame.image.load("./images/bullet-up.png"),
            pygame.image.load("./images/bullet-down.png")
    ]

    def __init__(self,display,id_tank,id_group,speed,x_start,y_start,x_end,y_end):
        self.display = display
        self.id = id_tank
        self.id_group = id_group
        self.speed = speed
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end

    def draw(self,positionBullet):
        self.display.blit(positionBullet,(self.x_start,self.y_start))

    def motion(self,positionBullet):
        self.x_start += self.speed
        self.draw(positionBullet)

    def colision(self):
        pass





















