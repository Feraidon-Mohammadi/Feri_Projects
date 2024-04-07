from arcad import ARCADE


class Second_Game(ARCADE):

    def __init__(self,name):
        self.name = name




    def play_game_2(self):

        def guess_number():

            print("Guess Number - not yet implemented! \n")

        return guess_number

if __name__ == "__main__":
   name= input("Enter your Name: ")
   game = Second_Game(name)
   game.ply()

#def __init__(self, name):
        #super().__init__(name,2)


















