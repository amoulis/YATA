# a small python script for testing text-based RPG

import character
import random
import event
import log
import utils
import save
import menu
import os

# INIT
player = character.Character()
menu.menu(player)
random.seed(); # random event

order = "go"
success = True
# DAEMON
os.system('cls')
utils.printFile("text/intro")

while player._life > 0 and order!="quit":
	order = input("What do you want to do ? [move - repare - status - save - load - quit]\n >>> ")

	if order == "move":
		if player.isEnergyEmpty():
			log.failure("You have no more energy. You will die alone, drifting in space")
			event.gameOver()
			break;
		else:
			player._energy = player._energy-1
			rand_event = random.randint(1,3)
			if rand_event == 1:
				success = event.eventNothing()
			elif rand_event == 2:
				success = event.eventBattle(player)
			else:
				success = event.eventSpaceStation(player)
	elif order == "repare":
		choice = input("How much energy to you want to consumme for charging shield ? \n >>> ")
		if utils.isInt(choice):
			if player._energy - int(choice) >= 0:
				player._energy = player._energy - int(choice)
				player._shield = player._shield + int(choice)
				if player._shield > player._shieldMax:
					player._shield = player._shieldMax
				log.information("Shield repared !")
			else:
				log.warning("You don't have enough energy to do that")
		else:
			log.debug("Not a good option. Try again please")

	elif order == "save":
		save.saveGame(player)
	elif order == "load":
		save.loadGame(player)
	elif order == "status":
		player.status()
	else:
		if order != "quit":
			print("Sorry not a valid option. Try again please")

	if player._life == 0 or success == False:
		event.gameOver()