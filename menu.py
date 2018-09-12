import pygame

from main import *

class Menu:
	DISPLAY_WIDTH, DISPLAY_HEIGHT = 1050, 700
	TEXTCOLOR = (29, 155, 1)
	MENUIMAGE = pygame.image.load('./images/menu.jpg')
	MENUIMAGE = pygame.transform.scale(MENUIMAGE, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

	def __init__(self, gameDisplay, x, y):
		self.gameDisplay = gameDisplay
		self.x = x
		self.y = y
		self.textPlay = 'Play'
		self.textExit = 'Exit'
		self.backgroundPlay = (x, x + 100, y , y + 45)
		self.backgroundExit = (x, x + 100, y + 50, y + 100)
		self.font = pygame.font.SysFont('arial', 50)

	def draw(self):

		textPlay = self.font.render(self.textPlay, True, Menu.TEXTCOLOR)
		textExit = self.font.render(self.textExit, True, Menu.TEXTCOLOR)
		self.gameDisplay.blit(textPlay, (self.x + 15, self.y + 5 ))
		self.gameDisplay.blit(textExit, (self.x + 15, self.y + 50 ))

	def checkPos(self, x, y):
		print(self.backgroundPlay);
		print(self.backgroundExit)
		if self.backgroundPlay[0] < x < self.backgroundPlay[1] and self.backgroundPlay[2]< y <self.backgroundPlay[3]:
			return 'play'
		elif(self.backgroundExit[0] < x < self.backgroundExit[1] and self.backgroundExit[2]< y < self.backgroundExit[3]):
			return 'exit'

def startMenu():
	exit = False
	# Initilize python
	pygame.init()
	# Set the size for the window
	gameDisplay = pygame.display.set_mode(WINDOW_SIZE)

	menu = Menu(gameDisplay, 450, 300)
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
					startTank(gameDisplay)
					pass

				# print(res, posX, posY, exit)
		
		gameDisplay.blit(Menu.MENUIMAGE, (0,0))
		menu.draw()

	    # Hide cursor
		pygame.mouse.set_visible(True)
		pygame.display.flip()

	pygame.quit()
	quit()