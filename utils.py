def isInt(str):
	try:
		int(str)
		return True
	except ValueError:
		return False

def printFile(path):
	f = open(path, 'r')
	content = f.read()
	print(content)
	f.close()
