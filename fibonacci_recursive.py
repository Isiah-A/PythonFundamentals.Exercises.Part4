def fibonnaci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return fibonnaci(number - 1) + fibonnaci(number - 2)

print(fibonnaci(11))
