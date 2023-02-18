from human import Human
from ai import AI

class Game():
    def __init__(self):
        pass
    
    def run_game(self):
        self.determine_players()
        self.initiate_players()
        while self.player1.score > 2 and self.player2.score > 2:
            self.play_round()
            pass
    
    def determine_players(self):
        print("How many human players would you like?")
        self.player_number = int(input("Please enter 0, 1, or 2"))
    
    def initiate_players(self):
        if self.player_number == 0:
            self.player1 = AI("AI 1")
            self.player2 = AI("AI 2")
        if self.player_number == 1:
            self.player1 = Human("Player")
            self.player2 = AI("AI")
        if self.player_number == 2:
            self.player1 = Human("Player 1")
            self.player2 = Human("Player 2")

    def play_round(self):
        pass

    def determine_winner(self):
        pass

    def play_again(self):
        pass