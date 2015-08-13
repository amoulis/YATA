import sys
from termcolor import colored
import colorama
colorama.init()

# Functions

def warning(str):
	print( colored("[WARN] ", 'orange') + str)

def critical(str):
	print(colored("[CRIT] ", 'red') + str)

def information(str):
	print("[INFO] " + str)

def success(str):
	print(  colored('[SUCC] ', 'green') + str)

def failure(str):
	print(colored("[FAIL] ", 'red') + str)

def debug(str):
	print("[DEBUG] " + str)