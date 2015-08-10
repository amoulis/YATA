import character
import log
import random

def eventNothing():
	print("The planet you found is empty, nothing to be done")
	return True

def eventBattle(player):
	print("Woaw ! An ennemy ship is here. Get ready for battle !")
	# generate ennemy ship
	ennemy = character.Character(5, 1, 5, 0, 0, 10, "ennemy")
	# Fight !
	turn = 0
	while ennemy._life != 0 and player._life != 0:
		order = input("What do you want to do ? [fight - escape - status] \n >>>")
		if order == "fight":
			if turn%2 == 0: # player's turn
				ennemy.getDamages(player.dealtDamages())
			else:
				player.getDamages(ennemy.dealtDamages())
		elif order == "escape":
			rand_event = random.randint(1,3)
			if rand_event == 2:
				log.success("Escaping suceeded !")
				return True
			else:
				log.failure("failed escape")
				player.getDamages(ennemy.dealtDamages())
		elif order == "status":
			player.status()
			ennemy.status()

		turn = turn + 1

	if ennemy._life == 0 and player._life != 0:
		log.success("You defeated the ennemy !")
		player.earnXP(10)
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