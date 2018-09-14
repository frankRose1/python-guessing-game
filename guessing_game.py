"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random
import math

name = input("Welcome to the number guessing game! Please enter your name: ")


def start_game():
    random_number = math.ceil(random.random() * 100)
    user_answer = int(input("Okay, {}, I'm thinking of a number between 1 and 100. Take your shot: ".format(name)))
    attempts = 1

    while user_answer != random_number:
      if user_answer < random_number:
        user_answer = int(input("It's higher, guess again: "))
        attempts += 1
      elif user_answer > random_number:
        user_answer = int(input("It's lower, guess again: "))
        attempts += 1

    print("You got it! It took you {} tries to figure it out!".format(attempts))
    play_again()


def play_again():
  user_response = input("Would you like to play again? (Enter yes/no) ")

  if user_response.lower() == 'yes':
      start_game()
  elif user_response.lower() == 'no':
      print("Thanks for playing, {}. I'll be here if you want to play again!".format(name))


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()


