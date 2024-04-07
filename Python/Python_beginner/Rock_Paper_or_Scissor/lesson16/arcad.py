import argparse
import sys

from lesson16.guess_number import Second_Game
from rps_game import First_Game
from rps_game import First_Game


class ARCADE:
	count = 0
	
	def __init__(self, name, playerchoice, count):
		self.name = name
		ARCADE.count += 1
		self.count = count
		self.playerchoice = playerchoice
	
	def play_game(self):
		if self.count >= 1 and self.count <= 3:
			number = int(input("give a Number to start the Game:\n [1]-for Rock paper Scissors\n [2]-for Guess number "
							   "\n [x]-for exit!\n\n "))
			
			print("Which game do you want to play?")
			if number == 1:
				#game1 = rps_game.play_r_p_s()
				game1 = First_Game(self.name)
				game1.play_r_p_s()

			elif number == 2:
				#game2 = ARCADE.guess_number.play_game_2()
				game2 = Second_Game(self.name)
				game2.play_game_2()

			elif number == "x".lower():
				print("\n 😍😍😍😍")
				print("thank you for Playing! \n")

				sys.exit(f"Bye {self.name}! 🖐🖐")
				
				
			else:
				play_again = f"{self.name}, Welcome back to the Arcade!"
				print(play_again)
				x = int(input("Which game do you want to play again?"))
				print(x)




def main():
	parser = argparse.ArgumentParser(description="Provides a personalized game experience.")
	parser.add_argument("-n", "--name", metavar="name", required=True, help="The name of the person playing the game.")
	args = parser.parse_args()
	
	arcade = ARCADE(args.name, playerchoice=1, count=3)
	arcade.play_game()


if __name__ == "__main__":
	main()