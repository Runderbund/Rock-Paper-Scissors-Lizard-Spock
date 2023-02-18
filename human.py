from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        gesture = input("Please choose a gesture (1-5): ")
        # Is there a way to blank the input? Don't want other player to see.