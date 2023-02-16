import random
from player import Player

class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def choose_gesture(self):
        self.gesture = random.randint(0, 4)