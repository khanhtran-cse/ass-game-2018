import random, os.path
import math

#import basic pygame modules
import pygame
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


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

def getTankImages(name):
    img = load_image(name)
    i = 0
    imgs = []
    while(i<36):
        imgs.append(pygame.transform.rotate(img,i*10))
        i+=1
    return imgs

def getShotImages():
    img = load_image('shot.png')
    i = 0
    imgs = []
    while(i<36):
        imgs.append(pygame.transform.rotate(img,i*10))
        i+=1
    return imgs

def getSpriteByPosition(position,group):
    for index,spr in enumerate(group):
        if (index == position):
            return spr
    return False