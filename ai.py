import random
from player import Player
from time import sleep

class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def choose_gesture(self):
        self.gesture = self.gesture_options[random.randint(0, 4)]
        sleep(0.5)
        print (f"{self.name} throws {self.gesture}.")