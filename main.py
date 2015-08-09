# a small python script for testing text-based RPG

import character
import random
import event

# INIT
player = character.Character()
ennemy = character.Character(5, 1, 5, 0, 0)
random.seed(); # random event

order = "go"
while player._life > 0 and order!="quit":
	order = input("What do you want to do ? [move - repare - save - quit]\n >>> ")

	if order == "move":
		if player.isEnergyEmpty():
			print("You have no more energy. You will die alone drifting in space")
			event.gameOver()
			break;
		else:
			player._energy = player._energy-1
			rand_event = random.randint(1,3)
			if rand_event == 1:
				event.eventNothing()
			elif rand_event == 2:
				event.eventBattle()
			else:
				event.eventSpaceStation()
	elif order == "repare":
		print("reparing...")
	elif order == "save":
		print("saving...")
	else:
		if order != "quit":
			print("Sorry not a valid option. Try again please")