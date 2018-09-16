"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random
import math

name = input("Welcome to the number guessing game! Please enter your name: ")
game_over = False
scores = []


def start_game():
	global game_over
	print_high_score()
	attempts = 1
	random_number = math.ceil(random.random() * 100)

	while game_over == False:
		try:
			user_answer = int(input("Okay, {}, I'm thinking of a number between 1 and 100. Take your shot: ".format(name)))
			if user_answer <= 0:
				raise ValueError

			while user_answer != random_number:
				if user_answer < random_number:
					user_answer = int(input("It's higher, guess again: "))
					attempts += 1
				elif user_answer > random_number:
					user_answer = int(input("It's lower, guess again: "))
					attempts += 1
		except ValueError:
			print("Uh oh! You entered an invalid value, try again.")
		else:
			print("You got it! It took you {} tries to figure it out!".format(attempts))
			game_over = True
			scores.append(attempts)
			play_again()


def play_again():
	global game_over
	user_response = input("Would you like to play again? (Enter yes/no) ")
	if user_response.lower() == 'yes':
		game_over = False
		start_game()
	else :
		print("Thanks for playing, {}. See ya next time!".format(name))


def get_high_score():
	""" Get the lowest number value and return it
	"""
	scores.sort()
	print(scores)
	high_score = scores[0]
	print(high_score)
	return high_score


def print_high_score():
	if len(scores) == 0:
		print("There is currently no high score to beat, try to change that!")
	elif len(scores) > 0:
		high_score = get_high_score()
		print("{} is the score to beat!".format(high_score))

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()


