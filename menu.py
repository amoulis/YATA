import character
import save
import sys

def menu(player):
	choice = ""
	while choice != "load" or choice != "play" or choice != "quit":
		choice = input("What do you want to do ?\n play \n load \n quit \n >>> ")
		player = character.Character()
		if choice == "load":
			save.load(player)
		if choice == "play":
			return;
		elif choice == "quit":
			sys.exit("good bye")