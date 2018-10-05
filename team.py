from const import *
from basetank import BaseTank

class Team: 

	def __init__(self, teamGroup, positions, angles, isAlly):
		self.teamSize = TEAM_SIZE
		self.teamGroup = teamGroup
		self.isAlly = isAlly
		for i in range(len(positions)):
			# print(pos[i])
			tank = BaseTank(positions[i], angles[i], isAlly)
			self.teamGroup.add(tank)

	# def 

	