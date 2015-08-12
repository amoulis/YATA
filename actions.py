import log

def actionRepare(player):
	if player._credits - 50 >= 0:
		player._life = player._lifeMax;
		player._credits = player._credits - 50
		log.information("Repare done !")
	else:
		log.warning("Sorry, you don't have enough credits")

def actionRecharge(player):
	if player._credits - 10 >= 0:
		player._energy = player._energy + 1
		player._credits = player._credits - 10
		if player._energy > player._energyMax:
			player._energy = player._energyMax
	else:
		log.warning("Sorry, you don't have enough credits")