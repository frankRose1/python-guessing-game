
import random
import math

print("Welcome to the number guessing game! Your goal is to try to figure our what number I'm thinking of.")
name = input("Please enter your name and we'll get started: ")
game_over = False
attempts = 1
scores = []


def start_game():
	global game_over
	global attempts
	print_high_score()
	random_number = math.ceil(random.random() * 100)
	print("Okay, {}, I'm thinking of a number between 1 and 100.".format(name))
	while game_over == False:
		try:
			user_answer = int(input("Take your shot: "))
			while user_answer != random_number:
				if user_answer < random_number:
					attempts += 1
					user_answer = int(input("It's higher, guess again: "))
				elif user_answer > random_number:
					attempts += 1
					user_answer = int(input("It's lower, guess again: "))
		except ValueError:
			attempts += 1
			print("Uh oh! You entered an invalid value, try again.")
		else:
			print("You got it! It took you {} tries to figure it out!".format(attempts))
			game_over = True
			scores.append(attempts)
			play_again()


def play_again():
	global game_over
	global attempts 
	user_response = input("Would you like to play again? (Enter yes/no) ")
	if user_response.lower() == 'yes':
		game_over = False
		attempts = 1
		start_game()
	else :
		print("Thanks for playing, {}. See ya next time!".format(name))


def get_high_score():
	""" Get the lowest number value and return it
	"""
	scores.sort()
	high_score = scores[0]
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


