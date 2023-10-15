from enum import Enum
from rps_game import rps
import argparse
import random
import sys


class ARCADE():
	def __init__(self, name):
		self.name = name
		self.play_rps = play_rps
		self.guess_number = guess_number
	
	
		
		


def play_rps(name='playerOne'):
	





	def main():
		parser = argparse.ArgumentParser(description="Provides a personalized game experience.")
		parser.add_argument("-n", "--name", metavar="name",required=True, help="The name of the person playing the game.")
		
		args = parser.parse_args()
		
		play_rps(args,name)


		args = parser.parse_args()
		
		rock_paper_scissors = rps(args.name)
		rock_paper_scissors()









#if __name__ == "__main__":
#	main(name)







"""
rps = 1
guess_number = 2


class RPS(Enum):
	ROCK = 1
	PAPER = 2
	SCISSORS = 3

	from rps_game import RPS
	import argparse
	import random
	import sys
	
	
	
	def get_player_count():
		return plyer_count
	
	def get_game_count():
		return game_count
	
	def get_python_wins():
		return python_wins
	
	def get_player_name():
		return name
	
	"""
"""
	playerchoice = input(f"{name} chose the Game you want to lunch\n,1 for Rock_paper_Scissors \n 2 for Guess Number")
	player = int(playerchoice)

	if player == 1 :
		#import rps
		rps.play_rps(name='playerOne')

"""


"""
#unneeded statement but usefull

	if __name__ == "__main__":
		name = input("Enter your name: ")
		arcade = Arcade(name)

"""



