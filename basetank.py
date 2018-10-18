
from const import *
from util import *
from bullet import Bullet
from Explosion import Explosion
from health import Health

class BaseTank(pygame.sprite.Sprite):

	speed = TANK_SPEED
	isVisible = False
	canShot = True
	size_image = (50,30)

	def __init__(self, position, angle, isAlly):
		pygame.sprite.Sprite.__init__(self)

		self.image_sprite1 = pygame.image.load('./data/tank-move-up3.png')
		self.image_sprite2 = pygame.image.load('./data/tank-move-up4.png')

		self.position = position
		self.isAlly = isAlly
		self.angle = angle
		if isAlly == True:
			self.tank1_image()
			self.health = Health(TANK_HP,1)
		else:
			self.tank2_image()
			self.health = Health(TANK_HP,2)
		self.hp = TANK_HP

		self.timeToReload = pygame.time.get_ticks()
		self.timeToChangeAI = pygame.time.get_ticks()

	def tank1_image(self):
		self.original_image = self.image_sprite1# self.image_sprite1.subsurface((0,0,42,100))
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect(center = self.position)

	def tank2_image(self):
		self.original_image = self.image_sprite2# self.image_sprite2.subsurface((0,0,42,100))
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect(center = self.position)


	def updateIsVisible(self, isVisible):
		self.isVisible = isVisible

	def move(self, direction):
		if(direction == "head"):
			self.position = newPosition(self.position, self.angle +90 , self.speed)
		elif(direction == 'left'):
			self.angle += TANK_ANGLE_TO_ROTATE
			self.angle %=360
			# self.position = newPosition(self.position, self.angle, self.speed)
		elif(direction == 'right'):
			self.angle -= TANK_ANGLE_TO_ROTATE
			self.angle %=360
			# self.position = newPosition(self.position, self.angle, self.speed)
		elif(direction == 'back'):
			self.position = newPosition(self.position, self.angle + 90, -self.speed)
		x, y = self.position
		if x <= 0:
			x = 0
		elif x >= WINDOW_WIDTH:
			x = WINDOW_WIDTH
		if y <=0:
			y =0
		elif y >= WINDOW_HEIGHT:
			y = WINDOW_HEIGHT
		self.position = (x,y)
		# print(self.angle)
		# print(self.position)

	def shot(self):
		if self.canShot:
			self.canShot = False
			if(self.isAlly):
				type = 1
			else:
				type = 2
			return Bullet(type,self.angle +90, newPosition(self.position, self.angle + 90, TANK_ALPHA_FOR_BULLET_FIRE))
		else:
			print("Need time to reload")
			return None

	def isShoted(self, hp):
		if hp < self.hp:
			self.hp -= hp
			# animation for shoted
		else:
			# animation for destroyed
			Explosion(self)
			self.kill()

	def setState(self, state):
		self.state = state

	def setInitState(self, state):
		self.initState = state
		self.state = state

	def perception(self, teamEnemy, flagEnemy, flagAlly):
		res = []
		for i in teamEnemy:
			# res.append(distance_eulic(self.position, i.position) )
			res.append((distance_eulic(self.position, i.position), i))
		target = min(res, key = lambda t: t[0])
		# print(target)

		if target[0] <= PERCEPTION_DISTANCE**2:
			print("*")
			return ('findEnemy', target[1])
		elif flagAlly.hp <= FLAG_HP_WARNING:
			return ('inDefend', flagAlly)
		elif flagEnemy.hp <= FLAG_HP_WARNING:
			return('inAttack', flagEnemy)
		else:
			distanceFlagEnemy = distance_eulic(self.position, flagEnemy.position)
			distanceFlagAlly = distance_eulic(self.position, flagAlly.position)
			if distanceFlagEnemy < PERCEPTION_DISTANCE**2:
				return ('stayAndShot', flagEnemy)
			elif distanceFlagAlly < PERCEPTION_DISTANCE**2:
				return ('stay', flagAlly)
			# stupid WIP: improve
			return self.initState


	def moveAt(self,target):
		angleVector = angleTwoPoint(self, target)
		# print(abs(angle), self.angle +90)
		angle = abs((angleVector-(self.angle+90) + 360)%360)
		if( angle < ANGLE_PERCENT) :
			self.move('head')
		else:
			if angle <180:
				# print(angle, angleVector, 'left')
				self.move('left')
			else:
				# print(angle, angleVector, 'right')
				self.move('right')
		pass

	def AI(self, teamEnemy, bulletGroup, flagEnemy, flagAlly):
		self.tmp = pygame.time.get_ticks()
		if self.tmp - self.timeToChangeAI  >= TIMER:
			self.timeToChangeAI = self.tmp
			self.state = self.perception(teamEnemy, flagEnemy, flagAlly)
		if (self.state[0] == 'findEnemy'):
			angleVector = angleTwoPoint(self, self.state[1])
			angle = abs((angleVector-(self.angle+90) + 360)%360)
			# print(angle, self.angle+90, angleVector)
			if( angle < ANGLE_PERCENT):
				if self.canShot  :
					print('shot')
					bulletGroup.add(self.shot())
				else:
					self.move('back')
			else:
				if angle <180:
					self.move('left')
				else:
					self.move('right')

		elif (self.state[0] == 'inAttack'):
			self.moveAt(self.state[1])
		elif (self.state[0] == 'inDefend'):
			self.moveAt(self.state[1])
		elif (self.state[0] == 'stayAndShot'):
			angleVector = angleTwoPoint(self, self.state[1])
			angle = abs((angleVector-(self.angle+90) + 360)%360)
			if( angle < ANGLE_PERCENT) :
				if self.canShot:
					print('shot')
					bulletGroup.add(self.shot())
			else:
				if angle <180:
					self.move('left')
				else:
					self.move('right')
			#WIP: need  impove
			# print('stay')

	def getRect(self):
		return self.rect

	def update(self):
		self.tmp = pygame.time.get_ticks()
		if (self.tmp - self.timeToReload > TANK_TIME_RELOAD):
			self.timeToReload = self.tmp
			self.canShot = True
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect(center = self.position)
		# self.rect = (self.position, (232 - 182,415-345))
		self.health.update(self,self.hp)

	def setActive(self,active):
		self.active = active