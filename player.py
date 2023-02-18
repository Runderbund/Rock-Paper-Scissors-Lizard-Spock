class Player:
    def __init__(self): 
        self.score = 0
        self.gesture_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
    def increase_score(self):
        self.score += 1