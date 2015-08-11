def saveGame(player):
	name = input("Enter the name of the save. \n >>> ")

	if name != "":
		f = open(name, 'w+')
		f.write( str(player._name)+ "\n")
		f.write( str(player._shield)+ "\n")
		f.write( str(player._life)+ "\n")
		f.write( str(player._strength)+ "\n")
		f.write( str(player._xp)+ "\n")
		f.write( str(player._credits)+ "\n")
		f.write( str(player._energy)+ "\n")
		f.write( str(player._dodge)+ "\n")
		f.write( str(player._energyMax)+ "\n")
		f.write( str(player._shieldMax)+ "\n")
		f.write( str(player._lifeMax)+ "\n")
		f.close()
		print("File saved as " + name)
	else:
		print("Sorry error in name of file try again")

def loadGame(player):
	name = input("Enter the name of the game you wish to load. \n >>> ")

	if name != "":
		f = open(name, 'r')
		player._name = f.readline()
		player._shield = int(f.readline())
		player._life = int(f.readline())
		player._strength = int(f.readline())
		player._xp = int(f.readline())
		player._credits = int(f.readline())
		player._energy = int(f.readline())
		player._dodge = int(f.readline())
		player._energyMax = int(f.readline())
		player._shieldMax = int(f.readline())
		player._lifeMax = int(f.readline())
		f.close()
		print("Game loaded !");
	else:
		print("Sorry error in name of file try again")
