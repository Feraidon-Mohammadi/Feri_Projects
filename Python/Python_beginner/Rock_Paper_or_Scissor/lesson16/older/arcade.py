import argparse
import rps_game
import guess_number


class ARCADE():
    count = 0

    def __init__(self,name , playerchoice, count):

        self.name = name
        ARCADE.count += 1
        self.count = count
        self.playerchoice = playerchoice

    def play_game(self):

        if self.count >= 1 and self.count <= 3:
            number = int(input("give a Number to start the Game: -1 for Rock paper Scissors , -2 for Guess number \n and -x for exit: "))

            print("Which game do you want to play?")
            if number ==1:
                game1 =rps_game.play_r_p_s()
                game1()
            elif number ==2:
               game2 = guess_number.play_game_2()
               game2()
            elif number == "x".lower():
                print(f"{self.name}, Welcome back to the Arcade!")
                x = int(input("Which game do you want to play?"))
                print(x)
            else:
                game3 = None




#def play_r_p_s(name='PlayerOne'):

def main():
    parser = argparse.ArgumentParser(description="Provides a personalized game experience.")
    parser.add_argument("-n", "--name", metavar="name", required=True, help="The name of the person playing the game.")
    args = parser.parse_args()

    arcade = ARCADE(args.name, playerchoice=1, count=3)
    arcade.play_game()

if __name__ == "__main__":
    main()
















"""
gameNumber = int(input("Which game do you want to play?"))
if gameNumber == 0:
    game = rps_game.play_r_p_s()
elif gameNumber == 1:
    game = guess_number.play_game_2()
else:
    game = None

if game:
    game()

"""


