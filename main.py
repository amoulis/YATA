# a small python script for testing text-based RPG

import character
import random
import event
import log

# INIT
player = character.Character()
random.seed(); # random event

order = "go"
success = True
# DAEMON
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
				success = event.eventNothing()
			elif rand_event == 2:
				success = event.eventBattle()
			else:
				success = event.eventSpaceStation()
	elif order == "repare":
		print("reparing...")
	elif order == "save":
		print("saving...")
	else:
		if order != "quit":
			print("Sorry not a valid option. Try again please")

	if player._life == 0 or sucess == False:
		event.gameOver()