# a small python script for testing text-based RPG

import character
import random
import event

# INIT
player = character.Character()
ennemy = character.Character(5, 1, 5, 0)
random.seed(); # random event

"""while player._life > 0:
	rand_event = random.randint(1,3)
	if rand_event == 1:
		event.eventNothing()
	elif rand_event == 2:
		event.eventBattle()
	else:
		event.eventSpaceStation()
	player.getDamages(ennemy.dealtDamages())
"""
print(player._shield)