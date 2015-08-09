class Character:

	def __init__(self, life=5, strength=5, shield=5, xp=0):
		self._life = life
		self._strength = strength
		self._shield = shield
		self._xp = xp

	def getDamages(self, damages):
		self._shield = self._shield - damages
		# if damages exceeded shield, dealt damages to life
		if self._shield != 0 & self._shield < 0:
			self._life = self.life + self._shield; # because shield < 0 no need to use '-'
			self._shield = 0
			print("[WARN] shield broken !")

	def dealtDamages(self):
		return self._strength

	def isAlive(self):
		if life == 0:
			return 1
		else:
			return 0