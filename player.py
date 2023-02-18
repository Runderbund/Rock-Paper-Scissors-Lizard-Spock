class Player:
    def __init__(self, name): 
        self.score = 0
        gesture_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
    def increase_score(self):
        self.score += 1