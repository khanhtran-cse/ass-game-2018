from const import *
from team import Team
from flag import Flag
from basetank import BaseTank

def main():
	clock = pygame.time.Clock()

	pygame.init()

	screen = pygame.display.set_mode(WINDOW_SIZE)

	background = pygame.image.load('./images/background.jpg')
	background = pygame.transform.scale(background, WINDOW_SIZE)

	# init team 
	posEnemy = [(200, 100),(400, 100), (650, 100), (900,100), (1100,100)]

	teamEnemyGroup = pygame.sprite.Group()
	Team(teamEnemyGroup,posEnemy, False)

	posAlly = [(200, 500), (400, 500), (650, 500), (900, 500), (1100,  500)]
	teamAllyGroup = pygame.sprite.Group()
	Team(teamAllyGroup,posAlly,  True)

	#player 
	playerTank = BaseTank((650, 300))
	playerTank.tank1_image()

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
			# if event.type == pygame.KEYDOWN:
			# 	if event.key == pygame.K_A:

			# 	else:

		screen.blit(background, (0,0))

		flagGroup.update()
		flagGroup.draw(screen)
		teamEnemyGroup.draw(screen)
		teamAllyGroup.draw(screen)

		screen.blit(playerTank.image, playerTank.pos)

		pygame.display.flip()
		clock.tick(FPS)

if __name__ == '__main__':
	main()
	