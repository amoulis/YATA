class Character:

	def __init__(self, life=5, strength=5, armor=5, xp=0):
		self._life = life
		self._strength = strength
		self._armor = armor
		self._xp = xp

	"""def getDamages(self, damages)

		if armor >= damages:
			armor = armor - 5
		else if armor < damages && 
		"""
	def isAlive(self):
		if life == 0:
			return 1
		else:
			return 0