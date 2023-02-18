from player import Player
from time import sleep

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        # Check input. Only allow 1-5
        # Adjusts down, so players don't have to deal with 0 indexing
        self.gesture = self.gesture_options(int(input("Please choose a gesture (1-5): "))-1)
            # Is this too compact/hard to parse? Also considered breaking into 2:
                # choice = int(input("Please choose a gesture (1-5): "))-1
                # self.gesture = self.gesture_options[choice]
            
        # Is there a way to blank the input? Don't want other player to see.
        sleep(0.75)
        print ("f{self.name} throws {self.gesture}.")