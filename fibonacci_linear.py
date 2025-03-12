def give_number():
   x = input("Give me a number between 0 and 30: ")
   return x

def fibonnaci(number):
    if number < 0 or number > 30:
        print("NOOOOOO!!!!")
    else:
        list = [0, 1]
        for f in range(2,number + 1, 1):
            newlist = [list[f-1]+list[f-2]]
            list = list + newlist
    print("Fibonnaci is " +str(list[number]))


gn = give_number()
fibonnaci(int(gn))