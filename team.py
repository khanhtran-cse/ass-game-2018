from const import *
from tankbase import BaseTank

class Team: 

	def __init__(self, pos):
		self.teamSize = TEAM_SIZE
		teamGroup = pygame.sprite.Group()

		for i in range(self.teamSize):
			tank = BaseTank(pos[i])
			teamGroup.add(tank)

	# def 

	