import random
from random import randrange

def number_checker(x,l):
	if int(x) == int(l):
		print("Correct")
	elif int(x) < int(l):
		print("Too low")
	elif int(x) > int(l):
		print("Too high")

def go_again():
	try_again = True
	while try_again:
		num = input("Give me a number between 1 and 10\n")
		number_checker(int(num), rando)
		if int(num) == int(rando):
			try_again = False




rando = random.randrange(10)
go_again()

#Putting random number into function then calling function kept
#creating a new random number when called


