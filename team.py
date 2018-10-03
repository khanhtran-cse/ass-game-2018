from const import *
from basetank import BaseTank

class Team: 

	def __init__(self, teamGroup, pos, isAlly):
		self.teamSize = TEAM_SIZE
		self.teamGroup = teamGroup
		for i in range(len(pos)):
			print(pos[i])
			tank = BaseTank(pos[i])
			if(isAlly):
				tank.tank1_image()
			else:
				tank.tank2_image()
			self.teamGroup.add(tank)

	# def 

	