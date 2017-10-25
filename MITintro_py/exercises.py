# In this problem, you'll create a program that guesses a secret number!
#
# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
#
# Here is a transcript of an example session:
#
# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 75?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 87?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
# Is your secret number 81?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 84?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
# Is your secret number 82?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 83?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
# Game over. Your secret number was: 83

import random
top = 100
bottom = 0
print("Please think of  a number between 0 and 100.")
while True:
    guess = input("Is your secret number {}? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ".format((top+bottom)//2))

    if guess == "l":
        bottom = (top+bottom)//2

    elif guess == "h":
        top = (top+bottom)//2

    elif guess == "c":
        print("Game over. Your secret number was: {}".format((top+bottom)//2))
        break
    else:
        print("Sorry, I did not understand your input.")
