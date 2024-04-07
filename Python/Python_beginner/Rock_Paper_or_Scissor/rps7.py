import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input("\nEnter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n ")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2,  or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n you chose {str(RPS(player)).replace('RPS.','').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.','').title()}.\n"
        )


        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3 :
                player_wins += 1
                return"🎉You win!"
            elif player == 2 and computer  == 1:
                player_wins += 1
                return"🎉You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉  You win !"
            elif player == computer:
                return"😆🤩 Tie Game!"
            else:
                python_wins += 1
                return "🤙 Python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n Game count  : { str(game_count)}")
        print(f"\n Player wins : { str(player_wins)}")
        print(f"\n Python wins : { str(python_wins)}")
        print(f"\n Play again?")

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
            sys.exit("Bye! 🖐🖐")

    return play_rps()

rock_paper_scissors = rps()

if __name__ == "__main__":
	rock_paper_scissors()
















