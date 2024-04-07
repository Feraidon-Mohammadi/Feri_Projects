import argparse
import sys
import random
from enum import Enum


def rps(name='PlayerOne'):
	game_count = 0
	player_wins = 0
	python_wins = 0
	
	def play_rps():
		nonlocal name
		nonlocal player_wins
		nonlocal python_wins
		
		class RPS(Enum):
			ROCK = 1
			PAPER = 2
			SCISSORS = 3
		
		
		playerchoice = input(
			f"\n{name},please enter...\n1 for Rock, \n2 for "
			f"Paper, or \n3 for Scissors: \n\n ")
		player = int(playerchoice)
		
		
		if playerchoice not in ["1", "2", "3"]:
			print(f"{name}, you must enter 1, 2, or 3.")
			return play_rps()
			
			
			
		computerchoice = random.choice("123")
		computer = int(computerchoice)
		
		
		print(f"\n{name} you chose {str(RPS(player)).replace('RPS.', '').title()}.")
		print(
			f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
		)
		
		def decide_winner(player, computer):
			nonlocal name
			nonlocal player_wins
			nonlocal python_wins
			
			if player == 1 and computer == 3:
				player_wins += 1
				return f"🎉{name} You win!"
			elif player == 2 and computer == 1:
				player_wins += 1
				return f"🎉{name} You win!"
			elif player == 3 and computer == 2:
				player_wins += 1
				return f"🎉{name} You win !"
			elif player == computer:
				return "😆🤩 Tie Game!"
			else:
				python_wins += 1
				return f"🤙 Python wins!\nSorry, {name}...😢"
		
		game_result = decide_winner(player, computer)
		
		print(game_result)
		
		nonlocal game_count
		game_count += 1
		
		print(f"\n Game count  : {game_count}")
		print(f"\n {name}'s wins : {player_wins}")
		print(f"\n Python wins : {python_wins}")
		print(f"\n Play again, {name} ?")
		
		while True:
			playagain = input("\nPlay again \nY for Yes or \nQ to Quit \n")
			if playagain.lower() not in ["y", "q"]:
				continue
			else:
				break
		
		if playagain.lower() == "y" or playagain.lower() == "Y":
			return play_rps()
		else:
			print("\n 😍😍😍😍")
			print("thank you for  Playing! \n")
			sys.exit(f"Bye {name}! 🖐🖐")
	
	return play_rps


if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description="Provides a personalized game experience."
	)
	
	parser.add_argument(
		"-n", "--name", metavar="name",
		required=True, help="The name of the person playing the game."
	)
	
	args = parser.parse_args()
	
	rock_paper_scissors = rps(args.name)
	rock_paper_scissors()
