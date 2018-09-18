
class Bullet:

	isStop = False

	def __init__(self, typ, damage, velocity, pos):
		self.typ = typ
		self.damage = damage
		self.velocity = velocity
		self.pos = pos

	def checkCollisionWithWall(self, map):
		pass

	def update():
		pass

	def render():
		pass

	def checkCollisionWithTarget(self, target):
		""" include collision with tank or enemy's home
		"""
		pass
