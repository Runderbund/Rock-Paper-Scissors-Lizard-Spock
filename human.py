from player import Player
from time import sleep
from getpass import getpass

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        print("\n1: Rock\n2: Paper\n3: Scissors\n4: Lizard\n5: Spock")
        self.gesture = input("Please choose a gesture (1-5): ")
        while not (self.gesture.isnumeric() and int(self.gesture) in [1, 2, 3, 4, 5]):
            self.gesture = input("Invalid input. Please enter an integer between 1 and 5: ")
        self.gesture = self.gesture_options[int(self.gesture)-1]# Adjusts down, so players don't have to deal with 0 indexing
        sleep(0.5)
        print (f"{self.name} throws {self.gesture}.")

        # Is there a way to blank the input? Don't want other player to see.
            # If so, I'd have to adjust the print statement to come after both players have made their choices.
            # There is: getpass
                # Only makes sense to use in 2-human games though
                # Just replace input with getpass