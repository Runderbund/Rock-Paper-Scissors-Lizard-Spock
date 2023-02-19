from human import Human
from ai import AI
from time import sleep

class Game():
    def run_game(self):
        self.determine_players()
        self.initiate_players()
        while self.player1.score < 2 and self.player2.score < 2:
            self.play_round()
        self.declare_game_winner()
        self.play_again()
    
    def determine_players(self):
        print("\nHow many human players would you like?")
        self.player_number = input("Please enter 0, 1, or 2: ")
        while not (self.player_number.isnumeric() and int(self.player_number) in [0, 1, 2]):
            self.player_number = input("Invalid input. Please enter either 0, 1, or 2: ")
        self.player_number = int(self.player_number)
        print ()
    
    def initiate_players(self):
        if self.player_number == 0:
            self.player1 = AI("AI 1")
            self.player2 = AI("AI 2")
        elif self.player_number == 1:
            self.player1 = Human("Player")
            self.player2 = AI("AI")
        elif self.player_number == 2:
            self.player1 = Human("Player 1")
            self.player2 = Human("Player 2")

    def play_round(self):
        self.player1.choose_gesture()
        self.player2.choose_gesture()
        self.determine_round_winner()

    def determine_round_winner(self):
        # Probably a better way to do this whole thing. 
            # Not sure how though. Putting in every single combination seems annoying but unavoidable.
        result = (self.player1.gesture, self.player2.gesture)
        sleep(0.5)
        if self.player1.gesture == self.player2.gesture:
            print (f"This round is a draw!\n")
        # elif result in [("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock"), ("Rock, Lizard"), ("Lizard", "Spock"), ("Spock", "Scissors"), ("Scissors", "Lizard"), ("Lizard", "Paper"), ("Paper", "Spock"), ("Spock", "Rock")]:
            # Better formatting to break out into lines?
        elif result in [
            ("Rock", "Scissors"), 
            ("Scissors", "Paper"), 
            ("Paper", "Rock"), 
            ("Rock, Lizard"), 
            ("Lizard", "Spock"), 
            ("Spock", "Scissors"), 
            ("Scissors", "Lizard"), 
            ("Lizard", "Paper"), 
            ("Paper", "Spock"), 
            ("Spock", "Rock")]:
            self.player1.increase_score()
            print (f"{self.player1.name} wins this round!\n")
        else:
            self.player2.increase_score()
            print (f"{self.player2.name} wins this round!\n")
    
    def declare_game_winner(self):
        # if (self.player1.score == 2):
        #     print (f"{self.player1.name} wins the game!")
        # else:
        #     print (f"{self.player2.name} wins the game!")        
        winner = self.player1.name if self.player1.score == 2 else self.player2.name
            # Found out about ternary operators, trying them out.
        print(f"The winner is {winner}!")
        
    def play_again(self):
        again = input("Would you like to play again? (y/n): ")
        while not again in ['y', 'n']:
            again = input("Please enter either y or n: ")
        if again == 'y':
            self.run_game()
        # Does this lead to a stack overflow eventually? 
        # If someone chooses yes 10 times, are all the other instances still waiting to close?