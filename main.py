from const import *
from team import Team
from flag import Flag

def main():
	clock = pygame.time.Clock()

	pygame.init()

	screen = pygame.display.set_mode(WINDOW_SIZE)

	background = pygame.image.load('./images/background.jpg')
	background = pygame.transform.scale(background, WINDOW_SIZE)

	# init team 
	# posEnemy = [(200, 100),(500, 100), (650, 100), (800,100), (1100,100)]
	# teamEnemy = Team(posEnemy)

	# posAlly = [(200, 600), (500, 600), (650, 1150), (800, 600), (1100,  600)]
	# teamAlly = Team(posAlly)

	# flag
	posFlagEnemy = (650, 20)
	posFlagAlly = (650, 620)

	flagEnemy = Flag(posFlagEnemy, True)
	flagAlly = Flag(posFlagAlly, False)

	flagGroup = pygame.sprite.Group()
	flagGroup.add(flagEnemy)
	flagGroup.add(flagAlly)

	exit = False
	while not exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True
		screen.blit(background, (0,0))

		flagGroup.update()
		flagGroup.draw(screen)

		pygame.display.flip()
		clock.tick(FPS)

if __name__ == '__main__':
	main()
	