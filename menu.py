import character
import save
import sys
import utils
import os

def menu(player):
	os.system('cls')
	choice = ""
	while choice != "load" or choice != "play" or choice != "quit":
		choice = input("What do you want to do ?\n play \n load \n rules \n quit \n >>> ")
		player = character.Character()
		if choice == "load":
			save.load(player)
		if choice == "play":
			return;
		elif choice == "quit":
			sys.exit("good bye")
		elif choice == "rules":
			os.system('cls')
			utils.printFile("text/rules")