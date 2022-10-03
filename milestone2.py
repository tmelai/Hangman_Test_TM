from curses.ascii import isalpha
from operator import truediv

alpha_input = True
while True: 
    guess = input(print("type in a valid character"))
    if guess.isalpha() != True: 
        print("Invalid letter. Please, enter a single alphabetical character.")
    else   : 
        alpha_input = FALSE
