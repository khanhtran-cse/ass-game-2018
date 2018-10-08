from const import *
from basetank import BaseTank

class Team: 

	def __init__(self, teamGroup, positions, angles, isAlly, flagAlly, flagEnemy, randomAttack):
		self.teamSize = TEAM_SIZE
		self.teamGroup = teamGroup
		self.isAlly = isAlly
		self.randomAttack = randomAttack
		for i in range(len(positions)):
			# print(pos[i])
			tank = BaseTank(positions[i], angles[i], isAlly)
			if random.random() <= randomAttack:
				tank.setInitState(('inAttack', flagEnemy))
			else:
				tank.setInitState(('inDefend', flagAlly))
			self.teamGroup.add(tank)

	# def 

	