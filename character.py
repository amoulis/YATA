class Character:

	def __init__(self, life=5, strength=5, armor=5, xp=0):
		self._life = life
		self._strength = strength
		self._armor = armor
		self._xp = xp

	def getDamages(self, damages):
		self._armor = self._armor - damages
		# if damages exceeded armor, dealt damages to life
		if self._armor != 0 & self._armor < 0:
			self._life = self.life + self._armor; # because armor < 0 no need to use '-'
			self._armor = 0
			print("[WARN] Armor broken !")

	def dealtDamages(self):
		return self._strength

	def isAlive(self):
		if life == 0:
			return 1
		else:
			return 0