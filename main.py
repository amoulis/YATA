# a small python script for testing text-based RPG

import character

# INIT
player = character.Character()
ennemy = character.Character(5, 1, 5, 0)


player.getDamages(ennemy.dealtDamages())
print(player._armor)