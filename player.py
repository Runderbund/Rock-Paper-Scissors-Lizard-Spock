class Player:
    def __init__(self): 
        self.score = 0
        self.gesture_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
            # Could set as a global constant in Game.
            # Would technically save on creating it for each player.
    
    def increase_score(self):
        self.score += 1