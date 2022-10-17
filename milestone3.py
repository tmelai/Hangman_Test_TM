
import random
from curses.ascii import isalpha
from operator import truediv

print("\nWelcome to Hangman\n")

class Hangman:
    def __init__(word_list, num_lives): 
        word = random.choice(word_list)
        word_guessed = list("_" * len(Hangman.word))
        num_lives = 5  
        list_of_guesses =[]


def play_game():
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry']
    game = Hangman(word_list,num_lives)
    game_on = True
    while game_on:
        if num_lives == 0:
            print("You lost")
            game_on = False
        if num_letters > 0 :
            ask_for_input()

        if num_lives !=0 and and num_letters not > 0 :
            print("Congratulations for winning the game")


def ask_for_input():   
    alpha_input = True
    while alpha_input: 
        guess = input(print("type in a valid character"))
        if guess.isalpha() != True and guess.len() !=1 : 
            print("Invalid letter. Please, enter a single alphabetical character.")
            ask_for_input()
        elif guess in list_of_guesses    :
            print("You already tried that letter!")
            ask_for_input()
        else   : 
            check_guess()


def check_guess(guess):
    guess.islower()
    if index != -1: 
        print("Sorry, {guess} is not in the word. Try again.")
        num_lives = num_lives-1
        print("You have {num_lives} lives left.")
    else: 
        print("Good guess! {guess} is in the word.")
    
    if guess not in list_of_guesses:
            list_of_guesses.append(guess)       

        
    for guess in word[::]:
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")


