from const import *

def main():
	clock = pygame.time.Clock()

	pygame.init()

	screen = pygame.display.set_mode(WINDOW_SIZE)

	background = pygame.image.load('./images/background.jpg')
	background = pygame.transform.scale(background, WINDOW_SIZE)
	exit = False
	while not exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True
		screen.blit(background, (0,0))


		pygame.display.flip()
		clock.tick(FPS)

if __name__ == '__main__':
	main()
	