



class Arcade_Main:
    def __init__(self):
        self.arcade = None
        self.first_game = None
        self.second_game = None

    def setup(self):
        name = input("Enter your Name: ")
        self.arcade = ARCADE(name)
        self.first_game = First_Game(name)
        self.second_game = Second_Game(name)

    def run(self):
        self.first_game.play_r_p_s()
        self.second_game.play_game_2()

if __name__ == "__main__":
    arcade_main = Arcade_Main()
    arcade_main.setup()
    arcade_main.run()






if __name__ == "__main__":
    name = input("Enter your Name: ")
    game = First_Game(name)
    game.play_r_p_s()