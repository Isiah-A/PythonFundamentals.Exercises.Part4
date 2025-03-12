import random
from random import randrange

def user_input():
	num = input("Give me a number between 1 and 10\n")
	number_checker(num)



def number_checker(num):
	"""
	checks random number in range
	 from 0 to 10
	 then checks if
	 an input is equal,
	 lesser or grater  
	 and prints out result
	"""
	rando = random.randrange(10)
	print("Your number was "+ str(num))
	print("The random number was "+ str(rando))
	if int(num) == int(rando):
		print("Correct")
	elif int(num) < int(rando):
		print("Too low")
	elif int(num) > int(rando):
		print("Too high")


user_input()

#Putting random number into function then calling function kept
#creating a new random number when called


