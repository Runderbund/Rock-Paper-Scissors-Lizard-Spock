from player import Player
from time import sleep

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        print("\n1: Rock\n2: Paper\n3: Scissors\n4: Lizard\n5: Spock")
        # Check input. Only allow 1-5
        # Adjusts down, so players don't have to deal with 0 indexing
        self.gesture = input("Please choose a gesture (1-5): ")
        while not (self.gesture.isnumeric() and int(self.gesture) in [1, 2, 3, 4, 5]):
            self.gesture = input("Invalid input. Please enter an integer between 1 and 5: ")
        self.gesture = int(self.gesture)        
        # self.gesture = self.gesture_options[int(input("Please choose a gesture (1-5): "))-1]
        
        
            # Is this too compact/hard to parse? Also considered breaking into 2:
                # choice = int(input("Please choose a gesture (1-5): "))-1
                # self.gesture = self.gesture_options[choice]
            
        # Is there a way to blank the input? Don't want other player to see.
        sleep(0.5)
        print (f"{self.name} throws {self.gesture}.")