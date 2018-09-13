import pygame

from main import *

class Menu:
	DISPLAY_WIDTH, DISPLAY_HEIGHT = 1050, 700
	TEXTCOLOR = (29, 155, 1)
	MENUIMAGE = pygame.image.load('./images/menu.jpg')
	MENUIMAGE = pygame.transform.scale(MENUIMAGE, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

	tron_yel = (255, 202, 0) 
	tron_regular = (255,   0,   0)
	tron_light = (255, 218,  10)

	def __init__(self, gameDisplay, x1, y1, x2, y2):
		self.gameDisplay = gameDisplay
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.play = ('Play', x1, y1, 50, 100, self.tron_yel )
		self.exit = ('Exit', x2, y2 , 50, 100, self.tron_yel )
		self.font = pygame.font.SysFont('arial', 50)


	def make_button(self, text, xpo, ypo, height, width, colour):
	    pygame.draw.rect(self.gameDisplay, self.tron_regular,
	                     (xpo - 10, ypo - 10, width, height), 3)
	    pygame.draw.rect(self.gameDisplay, self.tron_light,
	                     (xpo - 9, ypo - 9, width - 1, height - 1), 1)
	    pygame.draw.rect(self.gameDisplay, self.tron_regular,
	                     (xpo - 8, ypo - 8, width - 2, height - 2), 1)
	    font = pygame.font.Font(None, 42)
	    label = font.render(str(text), 1, (colour))
	    self.gameDisplay.blit(label, (xpo, ypo))

	def draw(self):
		self.make_button(*self.play)
		self.make_button(*self.exit)

	def checkPos(self, x, y):
		if self.play[1] < x < self.play[1]+ self.play[4] and self.play[2]< y <self.play[2] + self.play[3]:
			return 'play'
		elif(self.exit[1] < x < self.exit[1] + self.exit[4] and self.exit[2]< y < self.exit[2] + self.exit[3]):
			return 'exit'

def startMenu():
	exit = False
	# Initilize python
	pygame.init()
	# Set the size for the window
	gameDisplay = pygame.display.set_mode(WINDOW_SIZE)

	menu = Menu(gameDisplay, 460, 350, 460, 410)
	pygame.display.set_caption('Menu')
	menu.draw()

	while not exit: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True
			elif event.type == pygame.MOUSEBUTTONUP:
				(posX, posY) = pygame.mouse.get_pos()
				res = menu.checkPos(posX, posY)
				exit = (0,1)[res == 'exit']
				if res == 'play':
					exit = not startTank(gameDisplay)
					pass

		
		gameDisplay.blit(Menu.MENUIMAGE, (0,0))
		menu.draw()

	    # Hide cursor
		pygame.mouse.set_visible(True)
		pygame.display.flip()

	pygame.quit()
	quit()