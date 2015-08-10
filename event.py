import character

def eventNothing():
	print("The planet you found is empty, nothing to be done")
	return True

def eventBattle(player):
	print("Woaw ! An ennemy ship is here. Get ready for battle !")
	# generate ennemy ship
	ennemy = character.Character(5, 1, 5, 0, 0)
	# Fight !
	turn = 0
	while ennemy._life != 0 or player._life != 0:
		if turn%2 == 0: # player's turn
			ennemy.getDamages(player.dealtDamages())
		else:
			player.getDamages(ennemy.dealtDamages())
		turn = turn + 1

	if ennemy._life == 0 and player._life != 0:
		log.sucess("You defeated the ennemy !")
		return True
	elif player._life == 0 and ennemy._life != 0:
		log.failure("You've been defeated !")
		return False
	else:
		log.debug("Should not happen")
		return False

def eventSpaceStation(player):
	print("Welcome to a friendly space station. You can do some business here")
	return True

def gameOver():
	log.failure("It's game over, man ! Game Over !")