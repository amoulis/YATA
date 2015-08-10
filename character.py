"""
This class defines what a character is (player or PNJ) with different attributes
- life: when hits 0 the cahracter is dead
- shield : takes ammages before life does
- xp : is earned after combat and changes damages and dodge (TODO)
"""

class Character:

	def __init__(self, life=5, strength=5, shield=5, xp=0, dodge=0, energy=100):
		self._life = life
		self._strength = strength
		self._shield = shield
		self._dodge = dodge
		self._xp = xp
		self._energy = energy

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

	def isEnergyEmpty(self):
		if self._energy == 0:
			return True
		else:
			return False

	def status(self):
		if self._shield > 0:
			print("Shield: " + str(self._shield))
		else:
			log.warning("shield broken !")
		if self._energy < 10 and self._energy > 0:
			log.warning("energy low")
		elif self._energy == 0:
			log.critical("Energy Empty")

		log.info("Energy: " + str(self._energy))
		log.info("Strengh: " + str(self._strength))
		log.info("Life: " + str(self._life))
		log.info("Dodge: " + str(self._dodge))
		log.info("XP: " + str(self._xp))
