from const import *

class Bullet(pygame.sprite.Sprite):

	isStop = False
	speed = BULLET_SPEED

	def __init__(self, screen, typ, damage, vect, start_pos):
		"""type of buttle like laze, ... 
			vect: pygame.math.Vector2
		"""
		super().__init__()

		self.image = pygame.image.load('./images/bullet_25_25.jpg')
		self.size = self.image.get_rect().size

		self.screen = screen

		self.typ = typ
		self.damage = damage
		self.vect = vect
		self.start_pos = start_pos
		self.start_time = pygame.time.get_ticks()

		

	def checkCollisionWithWall(self, map):
		"""		width
			0---y--->
			|
			|x height
			|
		"""
		map_width, map_height = map.getSize()
		self.updatePos();
		(current_x, current_y) = self.pos
		if 0 < current_y < map_width  and 0 < current_x < map_height:
			return False
		return True

	def update():
		pass

	def updatePos(self):
		current_time = pygame.time.get_ticks()
		self.pos = (self.vect*(current_time - self.start_time)*self.speed + self.start_pos)

	def render():
		self.screen.blit(image, self.pos)

	def checkCollisionWithTarget(self, target):
		""" include collision with tank or enemy's home
		"""

