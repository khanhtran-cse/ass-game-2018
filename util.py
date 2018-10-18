import pygame,os.path
import math

#import basic pygame modules
import pygame
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0]

def sprite_sheet(size,file,pos=(0,0)):

    #Initial Values
    len_sprt_x,len_sprt_y = size #sprite size
    sprt_rect_x,sprt_rect_y = pos #where to find first sprite on sheet

    sheet = pygame.image.load(file).convert_alpha() #Load the sheet
    sheet_rect = sheet.get_rect()
    sprites = []
    # print (sheet_rect.height, sheet_rect.width)
    for i in range(0,sheet_rect.height,size[1]):#rows
        # print ("row")
        for i in range(0,sheet_rect.width,size[0]):#columns
            # print ("column")
            sheet.set_clip(pygame.Rect(sprt_rect_x, sprt_rect_y, len_sprt_x, len_sprt_y)) #find sprite you want
            sprite = sheet.subsurface(sheet.get_clip()) #grab the sprite you want
            sprites.append(sprite)
            sprt_rect_x += len_sprt_x
            # print(sprt_rect_x,  sprt_rect_y)
        sprt_rect_y += len_sprt_y
        sprt_rect_x = 0
    # print(sprites)
    return sprites

def newPosition(position, angle, speed):
    x, y = position
    xx =x + math.cos(math.radians(angle))* speed
    yy = y - math.sin(math.radians(angle))* speed
    # print(angle)
    return (xx,yy)

def subtract(position, delta):
    x, y = position
    deltaX, deltaY = delta
    return (x-deltaX, y-deltaY)

def collisionTankWithBullets(tank, bullets):
    x,y,w,h = tank.rect
    nWidth = 30
    rect = pygame.Rect(x + w/2-nWidth/2, y +  h/2-nWidth/2, nWidth, nWidth )
    for i in bullets:
        if i.rect.colliderect(rect):
            i.kill()
            return True
    return False

def collisionTankWithTank(tank, allTanks):
    x,y,w,h = tank.rect
    nWidth = 50
    rect = pygame.Rect(x + w/2-nWidth/2, y +  h/2-nWidth/2, nWidth, nWidth )
    for ortherTank in allTanks:
        if ortherTank != tank :
            x,y,w,h = ortherTank.rect
            rectOrther = pygame.Rect(x + w/2-nWidth/2, y +  h/2-nWidth/2, nWidth, nWidth )
            if(rectOrther.colliderect(rect)):
                return ortherTank
    return None

def distance_eulic(pos1, pos2):
    return abs(pos1[0] - pos2[0])**2 + abs(pos1[1] - pos2[1])**2 


def angleTwoPoint(a,b): # vector a => b
    return (pygame.math.Vector2(b.position[0]- a.position[0], b.position[1]- a.position[1]).angle_to((1,0)) +360)%360

class dummysound:
    def play(self): pass

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()
