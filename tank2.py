import pygame
# Set the height and width of the screen
screen_width = 1050
screen_height = 700
SCREENRECT = (screen_width,screen_height)

class Tank(pygame.sprite.Sprite):
    speed = 10
    images = []

    def __init__(self):
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(100,100))
        # self.top = 0
        # self.left = 0
        self.angle = 0

    def rotate(self, angle):
        self.angle += angle
        #todo: draw 

    def move(self, direction):
        # if direction: self.facing = direction
        self.rect.move_ip(direction*self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left//self.bounce%2)
        if(direction=='head'):
            self.rect.top += Tank.speed
        else:
            self.rect.top -= Tank.speed


    def gunpos(self):
        pos = self.facing*self.gun_offset + self.rect.centerx
        return pos, self.rect.top


pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])
Tank.images = [pygame.image.load('./images/tank-move-up.png')]
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

tank = Tank()
done = False


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# -------- Main Program Loop -----------
while not done:
    # Clear the screen
    screen.fill(WHITE)

    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
               tank.move('head')
            elif event.key == pygame.K_DOWN:
                tank.move('back')


    # --- Game logic

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 20 frames per second
    clock.tick(60)

pygame.quit()