
from ast import Break
import random
from curses.ascii import isalpha
from operator import truediv

# Start the game 

print("\nWelcome to Hangman\n")

class Hangman:

    def __init__(self,word_list,num_lives=5): 
            self.word = random.choice(word_list)
            self.word_guessed = list("_" * len(self.word))
            self.num_lives = num_lives
            self.list_of_guesses =[]
            self.num_letters = len(self.word)

    def ask_for_input(self):   
         
        guess = input("Guess a letter: ")
        if not guess.isalpha() or len(guess) !=1 : 
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses :
            print("You already tried that letter!")
        else   : 
            self.check_guess(guess)

            
            

    def check_guess(self,guess):
        guess = guess.lower()
        
        if guess in self.list_of_guesses:
            print(f"{guess} has been tried before - try another letter") 
            self.num_lives -= 1 
        elif guess in self.word: 
            print(f"Good guess! {guess} is in the word.")
            for index,letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index]= letter 
            self.num_letters -= 1
            ## self.list_of_guesses.append(guess)
            print(self.word_guessed)
        else :
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives = self.num_lives - 1
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)


def play_game(word_list):
    ##word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry']
    ##word_list = ['banana']
    game = Hangman(word_list)
  
    while True:
        if game.num_lives == 0:
            print("You've lost - better luck next time")
            break
        elif game.num_letters > 0 :
            game.ask_for_input()      
        else :
            print("Congratulations for winning the game")
            break
        

play_game(['banana'])       

