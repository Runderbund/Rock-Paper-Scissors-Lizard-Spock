from human import Human
from ai import AI
from time import sleep

class Game():
    def __init__(self):
        pass
    
    def run_game(self):
        self.determine_players()
        self.initiate_players()
        while self.player1.score < 2 and self.player2.score < 2:
            self.play_round()
        # I want a way to, in one line, check the score, and then print the winner based on who's higher.
        # Something like print (object that owns (max(self.player1.score, self.player2.score)))
        self.declare_game_winner()
    
    def determine_players(self):
        print("How many human players would you like?")
        self.player_number = input("Please enter 0, 1, or 2: ")
        while not (self.player_number.isnumeric() and int(self.player_number) in [0, 1, 2]):
            self.player_number = input("Invalid input. Please enter either 0, 1, or 2: ")
        self.player_number = int(self.player_number)
        print ()
    
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
        self.player1.choose_gesture()
        self.player2.choose_gesture()
        self.determine_round_winner()

    def determine_round_winner(self):
        result = (self.player1.gesture, self.player2.gesture)
        sleep(0.5)
        if self.player1.gesture == self.player2.gesture:
            print (f"This round is a draw!\n")
        elif result in [("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock"), ("Rock, Lizard"), ("Lizard", "Spock"), ("Spock", "Scissors"), ("Scissors", "Lizard"), ("Lizard", "Paper"), ("Paper", "Spock"), ("Spock", "Rock")]:
            # Want to break up line 41
            self.player1.increase_score()
            print (f"{self.player1.name} wins this round!\n")
        else:
            self.player2.increase_score()
            print (f"{self.player2.name} wins this round!\n")
    
    def declare_game_winner(self):
        if (self.player1.score == 2):
            print (f"{self.player1.name} wins the game!")
        else:
            print (f"{self.player2.name} wins the game!")
        
    def play_again(self):
        pass