import random
from player import Player

class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
